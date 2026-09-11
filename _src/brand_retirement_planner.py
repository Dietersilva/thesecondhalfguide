#!/usr/bin/env python3
"""Apply durable product branding to the retirement planner source before publish."""
from pathlib import Path

path = Path(__file__).with_name('retirement-strategy-model.html')
text = path.read_text(encoding='utf-8')
text = text.replace(
    '<span class="eyebrow">Interactive retirement planning tool</span>',
    '<span class="eyebrow">The Second Half Retirement Planner</span>',
    1,
)
path.write_text(text, encoding='utf-8')
print('retirement planner branding ready')
