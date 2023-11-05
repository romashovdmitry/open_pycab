# TO FIX: поискать возможность пройтись по ключам словарей, не указывая 
# напрямую. Ключи называются одинаково. 
def define_updated_fields(present_card: dict[str], previous_card: dict[str]):
    ''' define fields that was updated '''
    return_ = {}

    if present_card["text"] != previous_card["text"]:
        return_["updated_text"] = present_card["text"] 

    if present_card["text_definition"] != previous_card["text_definition"]:
        return_["updated_text_definition"] = present_card["text_definition"] 

    return return_
