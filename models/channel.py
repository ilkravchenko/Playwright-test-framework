from pydantic import BaseModel, Field
from faker import Faker


fake = Faker()


class CreateChannel(BaseModel):
    name: str = Field(default_factory=fake.name, alias='Channel name')
    client_revshare: str = Field(default_factory=lambda: str(fake.random_number(digits=2)), alias='Client\'s revshare')
