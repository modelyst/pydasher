#   Copyright 2021 Modelyst LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from typing import Optional

from pydantic import BaseModel

from pydasher.base import HashMixIn


class Address(BaseModel):
    number: str
    street: str


class Person(BaseModel):
    first_name: str
    last_name: str
    nickname: Optional[str]
    address: Optional[Address]


class Book(BaseModel):
    title: str
    author: Person
    publication_year: int


class BookWithPrice(BaseModel):
    _hashexclude_ = {"price"}
    title: str
    author: Person
    publication_year: int
    price: float


class Dummy(HashMixIn, BaseModel):
    key_1: str
    key_2: str
    key_3: float
    _hashexclude_ = {"key_3"}


class NestedDummy(HashMixIn, BaseModel):
    key_1: str
    key_2: Dummy
    key_3: float
    _hashexclude_ = {"key_3"}
