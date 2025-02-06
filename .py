import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# DATA
# -----------------------------------------------------------------------------
row_labels = [
    "Olson", 
    "Potter", 
    "Finley", 
    "Christenson", 
    "Walsh", 
    "Thomas", 
    "Triechel", 
    "Carney", 
    "Langlie", 
    "Johnson", 
    "Stuber"
]

col_labels = ["% Proficient", "4", "3", "2", "1", "N", "M", "Total Students"]

# Each row: [%Proficient, 4, 3, 2, 1, N, M, Total]
table_data = [
    ["42.86%",  0,  18, 17,  6, 1, 0,  42],
    ["43.59%",  0,  17, 17,  4, 1, 0,  39],
    ["68.60%",  0,  59, 13, 10, 4, 0,  86],
    ["61.76%",  1,  20, 10,  2, 1, 0,  34],
    ["78.48%",  2,  60, 12,  5, 0, 0,  79],
    ["68.18%",  0,  15,  2,  5, 0, 0,  22],
    ["58.23%",  0,  46, 23,  9, 1, 0,  79],
    ["75.00%",  0,  18,  4,  1, 1, 0,  24],
    ["86.96%",  0,  80, 12,  0, 0, 0,  92],
    ["63.89%",  1,  22, 11,  1, 1, 0,  36],
    ["68.18%",  0,  30, 10,  3, 1, 0,  44],
]

# -----------------------------------------------------------------------------
# CALCULATE TOTALS FOR 4, 3, 2, 1, N, M
# -----------------------------------------------------------------------------
# Indices for each column in table_data (beyond % Proficient):
#   4  => col index 1
#   3  => col index 2
#   2  => col index 3
#   1  => col index 4
#   N  => col index 5
#   M  => col index 6
# total students => col index 7

sum_4 = sum(row[1] for row in table_data)
sum_3 = sum(row[2] for row in table_data)
sum_2 = sum(row[3] for row in table_data)
sum_1 = sum(row[4] for row in table_data)
sum_N = sum(row[5] for row in table_data)
sum_M = sum(row[6] for row in table_data)

categories = ['4', '3', '2', '1', 'N', 'M']
counts     = [sum_4, sum_3, sum_2, sum_1, sum_N, sum_M]

# -----------------------------------------------------------------------------
# PLOT SETUP
# -----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(nrows=2, 
                               ncols=1, 
                               figsize=(10, 10), 
                               gridspec_kw={'height_ratios': [1, 1.5]})
# Main Title (spans entire figure)
fig.suptitle("Title of Assessment: Scientific Writing (SEP6 & SEP7)",
             fontsize=14, fontweight='bold')

# Sub-Title for the top chart
ax1.set_title("Game: Energy", fontsize=12)

# -----------------------------------------------------------------------------
# BAR CHART (Top)
# -----------------------------------------------------------------------------
ax1.bar(categories, counts, color='skyblue', edgecolor='black')
ax1.set_ylabel("Total Count")
ax1.set_xlabel("Score Category")
ax1.set_ylim(0, max(counts)*1.2)  # Add some headroom
# Optionally add numbers on top of each bar
for i, v in enumerate(counts):
    ax1.text(i, v + (max(counts)*0.02), str(v), 
             ha='center', va='bottom', fontweight='bold')

# -----------------------------------------------------------------------------
# TABLE (Bottom)
# -----------------------------------------------------------------------------
# Hide the axis for ax2 (we only want the table)
ax2.axis('off')

# Create the table in ax2
table = ax2.table(
    cellText=[row for row in table_data],
    rowLabels=row_labels,
    colLabels=col_labels,
    loc='center',
    cellLoc='center'
)

# Adjust table font size & scale
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.5)

# Adjust spacing so the titles and chart don’t overlap
plt.subplots_adjust(hspace=0.4)

# -----------------------------------------------------------------------------
# SAVE & SHOW
# -----------------------------------------------------------------------------
plt.savefig("assessment_graph_and_table.png", dpi=300, bbox_inches='tight')
plt.show()
