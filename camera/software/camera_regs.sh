# The syntax of the I2C write command is:
# szg_i2cwrite <linux device number> <camera address> <camera register> <register value>

szg_i2cwrite 0 0x18 0x31C6 0x84 # hispi_control[15:8]
szg_i2cwrite 0 0x18 0x31C7 0x00 # hispi_control[7:0]
szg_i2cwrite 0 0x18 0x3064 0x00 # Disable embedded Data
szg_i2cwrite 0 0x18 0x31AC 0x0A # uncompressed data bit width
szg_i2cwrite 0 0x18 0x31AD 0x0A # compressed data bit width
#szg_i2cwrite 0 0x18 0x31D1 0x1  # enable compression
szg_i2cwrite 0 0x18 0x306E 0x02 # datapath_select
szg_i2cwrite 0 0x18 0x302B 0x05 # vt_pix_clk_div
szg_i2cwrite 0 0x18 0x3031 0x31 # pll_multiplier
szg_i2cwrite 0 0x18 0x3037 0x0A  # op_pix_clk_div (data width)
szg_i2cwrite 0 0x18 0x3012 0x04 # Increase exposure time
szg_i2cwrite 0 0x18 0x3061 0x18 # Set gain to ISO 400
szg_i2cwrite 0 0x18 0x301C 0x1  # enable streaming
