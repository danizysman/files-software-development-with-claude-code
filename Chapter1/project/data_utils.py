def transform_records(records, multiplier=1.5, threshold=100):
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
