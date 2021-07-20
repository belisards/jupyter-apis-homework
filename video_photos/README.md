# ffmpeg

- Takes a frame from the video every second. %04d means four digits. Increase the r number to have more picutres. If there's 24 frames per second then you just have to put in 24.

`ffmpeg -i input.mp4 -r 1 output_%04d.png`

- Makes a grid

`montage -tile 3x0 -geometry +0+0 *.png grid.png`

- Resize images

`mogrify -resize 960x540 -quality 100 -path ./new-thumbs *.png`

- Without margins

`montage -tile 3x0 -geometry +0+0 *.png grid.png`

- Check metadata of the file

` exiftool timelapse.mp4 >a.txt`

- Download a PDF file 

`curl -L -o estatuto.pdf https://www.botafogo.com.br/transparencia/arquivos/BOTAFOGO-ESTATUTO-SOCIAL-2017-Gestao-Carlos-Eduardo.pdf`

- Convert it to images. You may need to change the ImageMagick's policy if it doesn't work on Ubuntu. [Check how here](https://askubuntu.com/questions/1181762/imagemagickconvert-im6-q16-no-images-defined)

`convert -density 72 estatuto.pdf -resize 25% report.png`

`convert -density 72 estatuto.pdf -resize 50% -background white -alpha remove -alpha off report-bigger.png`

- Create a grid from the images

`montage -tile 15x0 -geometry +0+0 report*.png grid.png`

- Create a GIF from the images. `loop 0` means infinite loop.

`convert -delay 10 report-bigger*png -loop 0 animate-estatuto.gif`