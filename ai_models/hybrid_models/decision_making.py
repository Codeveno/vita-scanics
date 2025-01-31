def hybrid_decision(image_data, text_data):
    """
    Combine image and text data for decision-making.
    """



    
    # Example: Simple weighted average
    image_score = image_data['confidence']  # Assume image_data is a dict with confidence
    text_score = text_data['score']  # Assume text_data is a dict with score
    final_score = 0.7 * image_score + 0.3 * text_score
    return final_score