import matplotlib.pyplot as plt # type: ignore

# Variant labels and corresponding Gibbs Free Energy (docking scores)
variants = ['Original', 'Delta', 'Omicron']
scores = [-70.90, -115.27, -152.39]  # More negative = stronger binding affinity

# Create figure and axis
fig, ax = plt.subplots()

# Plot each variant as a black dot
ax.scatter(variants, scores, color='black')

# Annotate each point with its corresponding score (slightly below the point)
for i, score in enumerate(scores):
    ax.text(variants[i], score - 5, f'{score}', ha='center')

# Set title and y-axis label
ax.set_title('Gibbs Free Energy of Binding for SARS-COV-2 Variants', fontsize=12, style='italic')
ax.set_ylabel('Docking Score (ΔG)')

# Invert y-axis to reflect that lower (more negative) energy is better binding
ax.set_ylim(0, -180)

# Add horizontal grid lines for visual clarity
ax.grid(True, linestyle='--', alpha=0.5)

# Optional aesthetics: remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()