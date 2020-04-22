SELECT FirstName, LastName, City, State
  FROM person
         LEFT JOIN address
             ON person.PersonID = address.PersonID;
