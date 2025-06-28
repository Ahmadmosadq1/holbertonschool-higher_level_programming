-- listing cities by states
SELECT cities.id, cities.name, states.name 
FROM hbtn_0d_usa
JOIN states 
  ON cities.state_id = states.id
ORDER BY cities.id