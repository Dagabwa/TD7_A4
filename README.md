Create a txt file on your computer and replace the path to the left of the ":" in the docker-compose.yml with that of your file.
`C:\Users\file.txt:/app/file.txt`

Then, build your app with : `docker-compose up`

Go to `http://localhost:5000/` to see the result.

You can modify your txt file on your computer. It will also change the txt in your container.