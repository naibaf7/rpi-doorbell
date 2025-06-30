# Service Setup
See `doorbell.service`.


# I2S Setup

Required in `/boot/config.txt`:

`dtparam=i2s=on`

`dtoverlay=hifiberry-dac`

reboot, configure audio with:

```
sudo raspi-config
1 System Options
S2 Audio
1 HifiBerry DAC HiFi pcm5102a-hifi-0
```

seems to work for I2S amp MAX98357, test with:
`speaker-test -l5 -c2 -t wav`

If the doorbell sound doesn't work when running as as service, check `cat /proc/asound/cards`
which gives:

```
 0 [Headphones     ]: bcm2835_headpho - bcm2835 Headphones
                      bcm2835 Headphones
 1 [sndrpihifiberry]: RPi-simple - snd_rpi_hifiberry_dac
                      snd_rpi_hifiberry_dac
 2 [vc4hdmi0       ]: vc4-hdmi - vc4-hdmi-0
                      vc4-hdmi-0
 3 [vc4hdmi1       ]: vc4-hdmi - vc4-hdmi-1
                      vc4-hdmi-1
```

and then insert the right number in `/etc/asound.conf`:

```
defaults.pcm.card 1
defaults.ctl.card 1
```