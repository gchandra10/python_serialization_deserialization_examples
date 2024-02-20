class friends_json_data:
    def simple_data(self):
        return {
            "characters": [
                {"name": "Ross Geller", "job": "Paleontologist", "age": 29},
                {"name": "Monica Geller", "job": "Chef", "age": 27},
                {"name": "Chandler Bing", "job": "Statistical analysis", "age": 30},
                {"name": "Joey Tribbiani", "job": "Actor", "age": 28},
                {"name": "Rachel Green", "job": "Fashion executive", "age": 27},
                {"name": "Phoebe Buffay", "job": "Masseuse and musician", "age": 30},
                {"name": "Richard", "job": "Dr", "age": 55},
                {"name": "Gunther", "job": "Owner", "age": 35},
                {"name": "Janice", "job": "None", "age": 28},
            ]
        }

    def nested_data(self):
        return [
            {
                "name": "Rachel Green",
                "occupation": "Fashion Executive",
                "relationship_status": "Single",
                "friends": [
                    "Ross Geller",
                    "Monica Geller",
                    "Joey Tribbiani",
                    "Chandler Bing",
                    "Phoebe Buffay",
                ],
                "education": {
                    "high_school": "Lincoln High School",
                    "college": "Not specified",
                },
                "employment_history": [
                    {
                        "company": "Central Perk",
                        "position": "Waitress",
                        "years": "1994-1995",
                    },
                    {
                        "company": "Bloomingdales",
                        "position": "Assistant Buyer",
                        "years": "1996-1999",
                    },
                    {
                        "company": "Ralph Lauren",
                        "position": "Executive",
                        "years": "1999-2004",
                    },
                ],
                "children": [],
            },
            {
                "name": "Ross Geller",
                "occupation": "Paleontologist",
                "relationship_status": "Divorced",
                "friends": [
                    "Rachel Green",
                    "Monica Geller",
                    "Joey Tribbiani",
                    "Chandler Bing",
                    "Phoebe Buffay",
                ],
                "children": [
                    {"name": "Ben Geller", "mother": "Carol Willick"},
                    {"name": "Emma Geller-Green", "mother": "Rachel Green"},
                ],
                "education": {
                    "college": "Columbia University",
                    "degree": "Ph.D. in Paleontology",
                },
                "employment_history": [],
            },
            {
                "name": "Monica Geller",
                "occupation": "Chef",
                "relationship_status": "Married",
                "friends": [
                    "Ross Geller",
                    "Rachel Green",
                    "Joey Tribbiani",
                    "Chandler Bing",
                    "Phoebe Buffay",
                ],
                "spouse": "Chandler Bing",
                "education": {"culinary_school": "Not specified"},
                "employment_history": [
                    {
                        "company": "Alessandros",
                        "position": "Head Chef",
                        "years": "Not specified",
                    },
                    {
                        "company": "Javu",
                        "position": "Chef",
                        "years": "Not specified",
                    },
                ],
                "children": [],
            },
            {
                "name": "Chandler Bing",
                "occupation": "Statistical analysis and data reconfiguration",
                "relationship_status": "Married",
                "friends": [
                    "Ross Geller",
                    "Monica Geller",
                    "Joey Tribbiani",
                    "Rachel Green",
                    "Phoebe Buffay",
                ],
                "spouse": "Monica Geller",
                "education": {"college": "Not specified"},
                "children": [],
                "employment_history": [],
            },
            {
                "name": "Phoebe Buffay",
                "occupation": "Masseuse and Musician",
                "relationship_status": "Married",
                "friends": [
                    "Ross Geller",
                    "Monica Geller",
                    "Joey Tribbiani",
                    "Chandler Bing",
                    "Rachel Green",
                ],
                "spouse": "Mike Hannigan",
                "education": {"high_school": "Not completed"},
                "children": [],
                "employment_history": [],
            },
            {
                "name": "Joey Tribbiani",
                "occupation": "Actor",
                "relationship_status": "Single",
                "friends": [
                    "Ross Geller",
                    "Monica Geller",
                    "Chandler Bing",
                    "Rachel Green",
                    "Phoebe Buffay",
                ],
                "education": {"drama_school": "Not specified"},
                "employment_history": [
                    {
                        "show": "Days of Our Lives",
                        "role": "Dr. Drake Ramoray",
                        "years": "Various",
                    }
                ],
                "children": [],
            },
        ]
