#!/usr/bin/env python3
"""
Create arXiv-style preprint PDF from ZENODO_PUBLIKATION.md
Format: A4, Times-Roman 10pt, margins 3cm/2.5cm/2.5cm/2.5cm
Tables: header #2C2C2C, alternating white/#F8F8F8
Code: Courier 8pt on #F5F5F5
Output: ADJ_System_v5.9f_Preprint.pdf
"""

import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --- Page Setup ---
MARGIN_TOP = 3.0 * cm
MARGIN_BOTTOM = 2.5 * cm
MARGIN_LEFT = 2.5 * cm
MARGIN_RIGHT = 2.5 * cm
PAGE_WIDTH, PAGE_HEIGHT = A4

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ADJ_System_v6.1_Preprint.pdf')

# --- Colors ---
C_HEADER_BG = HexColor('#2C2C2C')
C_HEADER_FG = white
C_ALT_ROW = HexColor('#F8F8F8')
C_CODE_BG = HexColor('#F5F5F5')
C_LINK = HexColor('#1A0DAB')
C_DARK = HexColor('#222222')
C_MUTED = HexColor('#555555')
C_RULE = HexColor('#CCCCCC')
C_KEYWORD = HexColor('#2C2C2C')

# --- Styles ---
styles = getSampleStyleSheet()

s_title = ParagraphStyle('Title', fontName='Times-Bold', fontSize=16, leading=20,
                         alignment=TA_CENTER, spaceAfter=4*mm, textColor=C_DARK)
s_subtitle = ParagraphStyle('Subtitle', fontName='Times-Italic', fontSize=11, leading=14,
                            alignment=TA_CENTER, spaceAfter=2*mm, textColor=C_MUTED)
s_meta = ParagraphStyle('Meta', fontName='Times-Roman', fontSize=9, leading=12,
                        alignment=TA_CENTER, spaceAfter=1*mm, textColor=C_MUTED)
s_abstract_head = ParagraphStyle('AbstractHead', fontName='Times-Bold', fontSize=10, leading=13,
                                 alignment=TA_LEFT, spaceBefore=6*mm, spaceAfter=2*mm)
s_abstract = ParagraphStyle('Abstract', fontName='Times-Roman', fontSize=10, leading=13,
                            alignment=TA_JUSTIFY, spaceAfter=4*mm,
                            leftIndent=4*mm, rightIndent=4*mm)
s_keywords = ParagraphStyle('Keywords', fontName='Times-Italic', fontSize=9, leading=12,
                            alignment=TA_LEFT, spaceAfter=6*mm, leftIndent=4*mm)
s_h1 = ParagraphStyle('H1', fontName='Times-Bold', fontSize=14, leading=17,
                      alignment=TA_LEFT, spaceBefore=8*mm, spaceAfter=4*mm, textColor=C_DARK)
s_h2 = ParagraphStyle('H2', fontName='Times-Bold', fontSize=12, leading=15,
                      alignment=TA_LEFT, spaceBefore=6*mm, spaceAfter=3*mm, textColor=C_DARK)
s_h3 = ParagraphStyle('H3', fontName='Times-Bold', fontSize=10.5, leading=14,
                      alignment=TA_LEFT, spaceBefore=4*mm, spaceAfter=2*mm, textColor=C_DARK)
s_body = ParagraphStyle('Body', fontName='Times-Roman', fontSize=10, leading=13,
                        alignment=TA_JUSTIFY, spaceAfter=2*mm)
s_body_indent = ParagraphStyle('BodyIndent', fontName='Times-Roman', fontSize=10, leading=13,
                               alignment=TA_JUSTIFY, spaceAfter=2*mm, leftIndent=4*mm)
s_enum = ParagraphStyle('Enum', fontName='Times-Roman', fontSize=10, leading=13,
                        alignment=TA_LEFT, spaceAfter=1.5*mm, leftIndent=8*mm,
                        firstLineIndent=-4*mm)
s_code = ParagraphStyle('Code', fontName='Courier', fontSize=8, leading=10,
                        alignment=TA_LEFT, spaceAfter=1*mm, leftIndent=2*mm,
                        backColor=C_CODE_BG)
s_code_block = ParagraphStyle('CodeBlock', fontName='Courier', fontSize=8, leading=10,
                              alignment=TA_LEFT, spaceBefore=2*mm, spaceAfter=2*mm,
                              leftIndent=4*mm, rightIndent=4*mm, backColor=C_CODE_BG)
s_table_cell = ParagraphStyle('TableCell', fontName='Times-Roman', fontSize=9, leading=12,
                              alignment=TA_LEFT, spaceBefore=1*mm, spaceAfter=1*mm)
s_table_header = ParagraphStyle('TableHeader', fontName='Times-Bold', fontSize=9, leading=12,
                                alignment=TA_LEFT, textColor=white, spaceBefore=1*mm, spaceAfter=1*mm)
s_footer = ParagraphStyle('Footer', fontName='Times-Italic', fontSize=8, leading=10,
                          alignment=TA_CENTER, textColor=C_MUTED)

# --- Markdown Parsing ---
def parse_markdown_line(line):
    """Convert inline markdown to ReportLab XML tags."""
    line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'\*(.+?)\*', r'<i>\1</i>', line)
    line = re.sub(r'`(.+?)`', r'<tt>\1</tt>', line)
    return line

def strip_markdown(line):
    """Strip markdown for simple text extraction."""
    line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
    line = re.sub(r'\*(.+?)\*', r'\1', line)
    line = re.sub(r'`(.+?)`', r'\1', line)
    return line

def split_table_row(line):
    """Split a table row line into cells."""
    parts = [p.strip() for p in line.split('|')]
    parts = [p for p in parts if p]
    return parts

def build_document(md_path):
    story = []
    lines = open(md_path, 'r', encoding='utf-8').read().split('\n')

    in_code_block = False
    code_buffer = []
    in_table = False
    table_header = []
    table_rows = []
    in_list = False
    list_counter = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # --- Code block handling ---
        if stripped.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_buffer)
                story.append(Paragraph(
                    code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    .replace(' ', '&nbsp;'),
                    s_code_block
                ))
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_buffer.append(stripped)
            continue

        # --- Skip separators ---
        if re.match(r'^---+$', stripped):
            story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE,
                                     spaceBefore=3*mm, spaceAfter=3*mm))
            continue

        # --- Empty line ---
        if not stripped:
            if in_table and table_header:
                story.append(build_table(table_header, table_rows))
                table_header, table_rows = [], []
                in_table = False
            in_list = False
            continue

        # --- Heading 1 (##) ---
        if stripped.startswith('## '):
            text = parse_markdown_line(stripped[3:])
            if text.startswith('Abstract'):
                story.append(Paragraph(text, s_h1))
            else:
                story.append(Paragraph(text, s_h1))
            continue

        # --- Heading 2 (###) ---
        if stripped.startswith('### '):
            text = parse_markdown_line(stripped[4:])
            story.append(Paragraph(text, s_h2))
            continue

        # --- Heading 3 (####) ---
        if stripped.startswith('#### '):
            text = parse_markdown_line(stripped[5:])
            story.append(Paragraph(text, s_h3))
            continue

        # --- Horizontal rule ---
        if stripped == '---':
            continue

        # --- Table row ---
        if stripped.startswith('|') and stripped.endswith('|'):
            cells = split_table_row(stripped)
            if not cells:
                continue
            # Check if it's a separator row
            if all(re.match(r'^[-:\s]+$', c) for c in cells):
                continue
            if not in_table:
                in_table = True
                table_header = cells
            else:
                table_rows.append(cells)
            continue

        # --- Bullet list ---
        if stripped.startswith('- ') or stripped.startswith('* '):
            text = parse_markdown_line(stripped[2:])
            story.append(Paragraph(f'&bull;&nbsp;{text}', s_body_indent))
            in_list = True
            continue

        # --- Numbered list (1. ...) ---
        m = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if m:
            num, text = m.group(1), parse_markdown_line(m.group(2))
            story.append(Paragraph(f'{num}.&nbsp;{text}', s_enum))
            in_list = True
            continue

        # --- Regular paragraph ---
        if stripped:
            text = parse_markdown_line(stripped)
            # Check if it's metadata line (bold key: value)
            if re.match(r'^\*\*.+?\*\*:', stripped):
                story.append(Paragraph(text, s_meta))
            else:
                story.append(Paragraph(text, s_body))

    # Flush remaining table
    if in_table and table_header:
        story.append(build_table(table_header, table_rows))

    return story


def build_table(header, rows):
    """Build a ReportLab Table from header and rows."""
    col_count = len(header)
    # Convert to Paragraphs for wrapping
    header_cells = [Paragraph(h, s_table_header) for h in header]
    data = [header_cells]
    for row in rows:
        # Pad or trim to col_count
        row_data = row[:col_count] + [''] * (col_count - len(row))
        data.append([Paragraph(parse_markdown_line(c), s_table_cell) for c in row_data])

    # Calculate column widths proportionally
    avail_width = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
    col_widths = [avail_width / col_count] * col_count

    t = Table(data, colWidths=col_widths, repeatRows=1)

    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), C_HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, 0), 4),
        ('GRID', (0, 0), (-1, -1), 0.4, C_RULE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]
    # Alternate row colors
    for idx in range(1, len(data)):
        if idx % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, idx), (-1, idx), C_ALT_ROW))
        else:
            style_cmds.append(('BACKGROUND', (0, idx), (-1, idx), white))

    t.setStyle(TableStyle(style_cmds))
    return t


def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Italic', 8)
    canvas.setFillColor(C_MUTED)
    # Header line
    canvas.drawString(MARGIN_LEFT, PAGE_HEIGHT - 1.2*cm,
                      'ADJ-System v6.1 — Preprint (nicht peer-reviewed)')
    canvas.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, PAGE_HEIGHT - 1.2*cm,
                           'Juli 2026')
    canvas.setStrokeColor(C_RULE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LEFT, PAGE_HEIGHT - 1.3*cm,
                PAGE_WIDTH - MARGIN_RIGHT, PAGE_HEIGHT - 1.3*cm)
    # Footer
    canvas.drawCentredString(PAGE_WIDTH / 2, 1.5*cm,
                             f'— {doc.page} —')
    canvas.drawString(MARGIN_LEFT, 1.0*cm,
                      '© 2026 Max Funk, Funk!Werk Ai Solutions — CC0')
    canvas.restoreState()


def create_pdf():
    md_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ZENODO_PUBLIKATION.md')
    
    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        title='ADJ-System: Advocatus Diaboli Judgment',
        author='Max Funk',
        subject='Epistemisches Falsifikationssystem für KI-generierte Abweichungen',
    )
    
    frame = Frame(MARGIN_LEFT, MARGIN_BOTTOM,
                  PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT,
                  PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM,
                  id='normal')
    
    template = PageTemplate(id='main', frames=[frame], onPage=add_header_footer)
    doc.addPageTemplates([template])
    
    # Build custom title block
    title_story = []
    title_story.append(Paragraph('ADJ-System: Advocatus Diaboli Judgment', s_title))
    title_story.append(Paragraph(
        'Ein epistemisches Falsifikationssystem f&uuml;r KI-generierte Abweichungen',
        s_subtitle
    ))
    title_story.append(Spacer(1, 3*mm))
    title_story.append(Paragraph(
        '<b>Theoretical Framework Paper | Preprint v6.1 — Juli 2026</b><br/>'
        'Nicht peer-reviewed. Zenodo-Preprint; keine Begutachtung.',
        s_meta
    ))
    title_story.append(Paragraph(
        '<b>Autoren:</b> Max Funk<br/>'
        '<b>Affiliation:</b> Funk!Werk Ai Solutions, Dorsten, Germany<br/>'
        '<b>Version:</b> v6.1 (2026-07-05, EPI-Suite, Live-Baselines, FEVER-Transfer)<br/>'
        '<b>Repository:</b> https://github.com/Masterq83/ADJ-System<br/>'
        '<b>DOI:</b> <a href="https://doi.org/10.5281/zenodo.21205393">10.5281/zenodo.21205393</a>',
        s_meta
    ))
    title_story.append(HRFlowable(width="100%", thickness=1, color=C_DARK,
                                   spaceBefore=4*mm, spaceAfter=4*mm))
    
    # Parse markdown body
    body_story = build_document(md_path)
    
    # Combine
    all_story = title_story + body_story
    
    doc.build(all_story)
    print(f"PDF created: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == '__main__':
    create_pdf()
