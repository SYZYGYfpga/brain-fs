% This is a quick and easy script that can be used to display image data for
% the Opal Kelly SYZYGY Camera Pod. Note that there is no Bayer transform
% performed on the image so it will not have color.

raw_image_file = fopen('capture.bin');

y = 2304;
z = 1296;

[raw_image_data,x] = fread(raw_image_file, [1, y*z], 'uint8');

raw_image_data_flip = flip(raw_image_data);

xx = double(reshape(raw_image_data_flip,y,z));

image = uint8(transpose(xx));

imshow(image);
