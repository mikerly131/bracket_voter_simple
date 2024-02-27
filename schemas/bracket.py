"""
Pydantic classes for brackets, translation between routes and db
"""
from pydantic import BaseModel
from typing import Optional, List, ForwardRef


class Bracket(BaseModel):
    id: int
    name: str
    user_id: int
    song_list_id: int
    pool_size: int
    ranking_type: str
    bracket_status: str
    seed_list: Optional[list]


# For relationships, commented out until I decide ot use them
#
# User = ForwardRef('User')
# FilledBracket = ForwardRef('FilledBracket')
#
#
# class BracketDetails(Bracket):
#     user: Optional[User]
#     filled_brackets: Optional[List[FilledBracket]] = []
#
#
# from .account import User
# from .filled_bracket import FilledBracket
# BracketDetails.update_forward_refs()
