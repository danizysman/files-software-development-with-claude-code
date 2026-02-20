"""Exercise variant: same idea as video process_data, different name and fields."""

def transform_records(records, multiplier=1.5, threshold=100):
    """Process financial records for quarterly reporting.

    Filters records above threshold, applies multiplier adjustment,
    and returns top performers sorted by adjusted value.
    """
    output = []
    for rec in records:
        val = rec.get('amount', 0)
        if val > threshold:
            adjusted = val * multiplier
            status = 'high' if adjusted > 200 else 'medium'
            output.append({
                'id': rec['id'],
                'original': val,
                'adjusted': adjusted,
                'status': status
            })
    return sorted(output, key=lambda x: x['adjusted'], reverse=True)[:5]
