delimiter_pairing_tests = [
    # === BASIC CASES ===
    {
        "description": "Basic single and double match",
        "input": "Before $a + b$ and $$x = y$$ after",
        "expected_single_pairs": [(7, 13)],
        "expected_double_pairs": [(19, 26)],
        "output": "Before \\(a + b\\) and \\[x = y\\] after"
    },
    {
        "description": "Only block math",
        "input": "$$x + y = z$$",
        "expected_single_pairs": [],
        "expected_double_pairs": [(0, 11)],
        "output": "\\[x + y = z\\]"
    },
    {
        "description": "Only inline math",
        "input": "Calculate $a = b$.",
        "expected_single_pairs": [(10, 16)],
        "expected_double_pairs": [],
        "output": "Calculate \\(a = b\\)."
    },

    # === OVERLAP & NESTING ===
    {
        "description": "Overlapping: $ $$X+Y$ XZ+K$$",
        "input": "$ $$X+Y$ XZ+K$$",
        "expected_single_pairs": [], 
        "expected_double_pairs": [(2, 13)],
        "output": "$ \\[X+Y$ XZ+K\\]"
    },
    {
        "description": "Nested single inside double — ignored",
        "input": "$$A $B$ C$$ and $D$",
        "expected_single_pairs": [(16, 18)],
        "expected_double_pairs": [(0, 9)],
        "output": "\\[A $B$ C\\] and \\(D\\)"
    },
    {
        "description": "Single open into math block",
		"input": "$Opening $$ $$",
		"expected_single_pairs": [],
        "expected_double_pairs": [(9, 12)],
        "output": "$Opening \\[ \\]"
	},

    # === RIGHTMOST-OPEN PREFERENCE ===
    {
        "description": "Two opens, one close — rightmost open wins",
        "input": "$bad $good$",
        "expected_single_pairs": [(5, 10)],
        "expected_double_pairs": [],
        "output": "$bad \\(good\\)"
    },
    {
        "description": "Three opens, two closes — pair rightmost valid openings",
        "input": "$a $b $c$ d$",
        "expected_single_pairs": [(6, 8)],
        "expected_double_pairs": [],
        "output": "$a $b \\(c\\) d$"
    },

    # === INVALID OPEN/CLOSE ===
    {
        "description": "Invalid single dollar opening (followed by space)",
        "input": "This $ is not math $x$",
        "expected_single_pairs": [(19, 21)],
        "expected_double_pairs": [],
        "output": "This $ is not math \\(x\\)"
    },
    {
        "description": "Unmatched closing",
        "input": "100$ is a price",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "100$ is a price"
    },
    {
        "description": "Unmatched double",
        "input": "$$unfinished block",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$$unfinished block"
    },
    {
        "description": "Invalid Close",
        "input": "$x $",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$x $"
    },
    {
        "description": "Invalid Open",
        "input": "$ x$",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$ x$"
    },
    {
        "description": "Single Non-closed Start",
        "input": "$x",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$x"
    },
    {
        "description": "Double Non-closed Start",
        "input": "$$x",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$$x"
    },
    {
        "description": "Single Non-closed End",
        "input": "x$",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "x$"
    },
    {
        "description": "Double Non-closed End",
        "input": "x$$",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "x$$"
    },

    # === MULTIPLE BLOCKS ===
    {
        "description": "Multiple $$ blocks",
        "input": "$$block1$$ text $$block2$$",
        "expected_single_pairs": [],
        "expected_double_pairs": [(0, 8), (16, 24)],
        "output": "\\[block1\\] text \\[block2\\]"
    },
    {
        "description": "Multiple blocks mixed",
        "input": "$$x^2$$ text $x+3$$x-7$",
        "expected_single_pairs": [(13,17),(18,22)],
        "expected_double_pairs": [(0, 5)],
        "output": "\\[x^2\\] text \\(x+3\\)\\(x-7\\)"
    },
    

    # === MIXED & ADJACENT ===
    {
        "description": "Adjacent delimiters",
        "input": "$x$$$y$",
        "expected_single_pairs": [(0, 2)],
        "expected_double_pairs": [],
        "output": "\\(x\\)$$y$"
  
    },
    {
        "description": "Empty inline and block",
        "input": "$$  $$ and $ $",
        "expected_single_pairs": [],
        "expected_double_pairs": [(0, 4)],
        "output": "\\[  \\] and $ $"
    },

    # === INLINE AT BOUNDARIES ===
    {
        "description": "Inline at start and end of string",
        "input": "$x+y$",
        "expected_single_pairs": [(0, 4)],
        "expected_double_pairs": [],
        "output": "\\(x+y\\)"
    },
    {
        "description": "Block at start and end",
        "input": "$$x+y$$",
        "expected_single_pairs": [],
        "expected_double_pairs": [(0, 5)],
        "output": "\\[x+y\\]"
    },

    # === INLINE ACROSS BLOCK BOUNDARY (DISALLOWED) ===
    {
        "description": "Inline $ inside block $$ ignored",
        "input": "$$a + $b$ + c$$ $d$",
        "expected_single_pairs": [(16, 18)],
        "expected_double_pairs": [(0, 13)],
        "output": "\\[a + $b$ + c\\] \\(d\\)"
    },
    {
        "description": "Space from start",
        "input": "$ a$",
        "expected_single_pairs": [],
        "expected_double_pairs": [],
        "output": "$ a$"
    },
    {
        "description": "Greedy Match",
        "input": "$a $b$ c$",
        "expected_single_pairs": [(3,5)],
        "expected_double_pairs": [],
        "output": "$a \\(b\\) c$"
    }, 
]
