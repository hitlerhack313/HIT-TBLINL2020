import base64
x = ( b'''ZnJvbSB0aW1lIGltcG9ydCBzbGVlcCBhcyB0aW1lb3V0CmltcG9ydCBzb2NrZXQKaW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKb3MuIHN5c3RlbSgiY2xlYXIiKQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMjIyMgVEhJUyBQWVRIT04gRklMRSBXQVMgV1JJVEVEIE9OIDIxLzcvMjAyMAojIyMjIyMjIyBWSUEgUFlUSE9OIExBTkdVQUdFIE9OTFkKIyMjIyBXQVMgV1JQR1JBTUVEIEJZIE0zTE9NQVQgVEhFIFBIT05FIE9OTFkKIyMjIyMjIyBUSElTIFNDUklCVCBIQVZFIExJTlNFQyAoMF8wKQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCmExID0iXGVbMDszMG0iICAgICAgICAjIEJsYWNrCmEyID0iXGVbMDszMW0iICAgICAgICAjIFJlZAphMyA9IlxlWzA7MzJtIiAgICAgICAgIyBHcmVlbgphNCA9IlxlWzA7MzNtIiAgICAgICAgIyBZZWxsb3cKYTUgPSJcZVswOzM0bSIgICAgICAgICMgQmx1ZQphNiA9IlxlWzA7MzVtIiAgICAgICAgIyBQdXJwbGUKYTcgPSJcZVswOzM2bSIgICAgICAgICMgQ3lhbgphOCA9IlxlWzA7MzdtIiAgICAgICAgIyBXaGl0ZQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjCiMgQm9sZCAjCiMjIyMjIyMKYjEgPSJcZVsxOzMwbSIgICAgICAgICMgQmxhY2sKYjIgPSJcZVsxOzMxbSIgICAgICAgICMgUmVkCmIzID0iXGVbMTszMm0iICAgICAgICAjIEdyZWVuCmI0ID0iXGVbMTszM20iICAgICAgICAjIFllbGxvdwpiNSA9IlxlWzE7MzRtIiAgICAgICAgIyBCbHVlCmI2ID0iXGVbMTszNW0iICAgICAgICAjIFB1cnBsZQpiNyA9IlxlWzE7MzZtIiAgICAgICAgIyBDeWFuCmI4ID0iXGVbMTszN20iICAgICAgICAjIFdoaXRlCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCmIgPSJcMDMzWzA7OTFtIiAgICAgICMgUkVECmYgPSJcMDMzWzE7OTJtIiAgICAgICMgR1JFRU4KYyA9IlwwMzNbMTs5Nm0iICAgICAgIwpsID0iXDAzM1sxOzk0bSIgICAgICAjCnYgPSJcMDMzWzA7MTAxbSIgICAgICMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpkZWYgbG9nbyAoKSA6CiAgICBwcmludCAoIiIpCiAgICBwcmludCAoIiAgICAgID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHByaW50IChiKyIgICAgICAgICAgIF9fX19fXyAgX18gICAgICBfXyAgICAgICBfX19fX18gICBfXyAgIF8gICBfICAgICAgIF9fICBfXyAgICAgICBfX19fXyAgICBfX19fXyAiKQogICAgcHJpbnQgKGYrIiAgICAgICAgICAvIF9fX18vIC8gLyAgICAgLyAgfCAgICAgLyBfX19fLyAgLyAvIC4nLicgfCB8ICAgICAvIC8gLyAgfCAgICAgLyBfICAgfCAgLyBfX18vICIpCiAgICBwcmludCAoYisiICAgICAgICAgLyAvX19fICAvIC8gICAgIC8gTCB8ICAgIC8gLyAgICAgIC8gLy0nLicgICB8IHwgXyAgLyAvIC8gTCB8ICAgIC8gL18pIC8gIC8gL19fICAgIikKICAgIHByaW50IChmKyIgICAgICAgIC9fX18gIC8gLyAvICAgICAvIF8gIHwgICAvIC8gICAgICAvIF8gIHwgICAgIHwgfC8gfC8gLyAvIF8gIHwgICAvIF8gICwnICAvIF9fXy8gICAiKQogICAgcHJpbnQgKGIrIiAgIF9fICBfX19fLyAvIC8gL19fXyAgLyAvIHwgfCAgLyAvX19fXyAgLyAvIHwgfCAgICAgfCAgL3wgIC8gLyAvIHwgfCAgLyAvIHwgfCAgLyAvX18gICAgICIpCiAgICBwcmludCAoZisiICAvIC8gL19fX19fLyAvX19fX18vIC9fLyAgfF98IC9fX19fX18vIC9fLyAgfF98ICAgICB8Xy8gfF8vIC9fLyAgfF98IC9fLyAgfF98IC9fX19fLyAgICAgIikKICAgIHByaW50IChiKyIgLyAvX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiKQogICAgcHJpbnQgKGIrIi9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy8gICBMICAgSSAgIE4gICBVICAgWCAgICAgICAgICIpCiAgICBwcmludCAoZisiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIikKICAgIHByaW50ICgiID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHByaW50ICgiICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrIikKICAgIHByaW50ICgiICsgKDBfKykgPj4+IEJZIE0zTE9NQVQgVEhFIFBIT05FICAgIFdJVEggICAgICBNRU5BIE1BR0RZRSAgICAgIDw8PCAoMF8rKSArIikKICAgIHByaW50ICgiICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrIikKICAgIHByaW50ICgiID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHByaW50ICgiICAgICAgICAgICAgICAgIFRISVMgVE9PTCBIQVMgQkVFTiBQUk9HUkFNRUQgVE8gVEwtV043MjJOICAgICAgICAgICAgICAgICAgIikKICAgIHByaW50ICgiIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIikKICAgIHByaW50ICgiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIikKbG9nbyAoKQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwpkZWYgcGFzc3MgKCkgOgogICAgdiA9IGlucHV0IChjKyJFTlRFUiBZT1VSIEJBU1NXT1JEIFRPIFNUQVJUID09PiAiKQogICAgaWYgdiA9PSAnSElUTEVSIEVHWSc6CiMgICAgICAgaWYgdiA9PSAnSElULVRCIE0zTE9NQVQnOgojICAgICAgIG9yIHYgPT0gJ01JTkEnIG9yIHYgPT0gJ2thbGlpaWlpJyA6CiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgdGltZS5zbGVlcCgwLjEpCiAgICAgICAgcHJpbnQgKCIiKQogICAgZWxzZToKIyAgICAgICB0KDAuMSwiXG5cdCAgICAgICAgICAgIFBMRUFTRSBXQUlUIC4uLi4iKQogICAgICAgIG9zLnN5c3RlbSgiZmlnbGV0ICsuLiBFUk9SUiAuLisiKQogICAgICAgIHByaW50ICgiICAgICAgICAgICAgICAgICAgICAgICAgICAgIF9fX19fX18gICAgICAgICAgICAgICAgICAgICAgICAgIikKICAgICAgICBwcmludCAoIiAgfC4uLi4uLi4uLi4uLi4uLi4uICheX14pIHwgRVJPUlIgfCAoXl9eKSAuLi4uLi4uLi4uLi4uLi4ufCIpCiAgICAgICAgcHJpbnQgKCIgIHwgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLS0tLSAgICAgICAgICAgICAgICAgICAgICAgIHwiKQogICAgICAgIHRpbWVvdXQoMC4zKQogICAgICAgIHByaW50ICgiICB8Li4uLi4uLi4uLi4uLi4uLi4uIFBBU1NXT1JTIElOQ09SRUNUIC4uLi4uLi4uLi4uLi4uLi4uLi58IikKICAgICAgICBwcmludCAoIiAgfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfCIpCiAgICAgICAgcHJpbnQgKGIrIiA9PT09PT09PT09PT09PT09PT09IFlPVSBDQU4gR0VUIEJBU1NXT1JEIElOID09PT09PT09PT09PT09PT09PT09ICIpCiAgICAgICAgcHJpbnQgKGYrInwgICAgICAgICAgICAgd3d3Lm0zbG9tYXR0aGVwaG9uZS5ibG9nc3BvdC5jb20gICAgICAgICAgICAgICAgICAgfCIpCiAgICAgICAgcHJpbnQgKGYrInwgICAgICAgICBodHRwczovL3QubWUvam9pbmNoYXQvTlltbFZoUGJDVTl0Zkd4QWVTYVozQSAgICAgICAgICAgfCIpCiAgICAgICAgcHJpbnQgKGYrInwgID09PT4gKCspIGh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL2MvbTNsb21hdHRoZXBob25lICgrKSA8PT09ICAgfCIpCiAgICAgICAgcHJpbnQgKGYrInwgICAgICAgICAgICAgICAgICAgVEhJUyBUT09MIEJZIE1FTkEgTUFHRFkgICAgICAgICAgICAgICAgICAgICAgfCIpCiAgICAgICAgcHJpbnQgKGIrIiA9PT09PT09PT09PT09PT09PT09PT09IFZJU0lUIFVTIElOIFRISVMgPT09PT09PT09PT09PT09PT09PT09PT09ICIpCiAgICAgICAgb3Muc3lzdGVtKCJleGl0IikKICAgICAgICBvcy5zeXN0ZW0gKCJISVQtVEIucHkiKQogICAgICAgIHRpbWUuc2xlZXAoMTApCiAgICAgICAgdGltZW91dCgwLjMpCiAgICAgICAgb3Muc3lzdGVtKCJzdWRvIGV4aXQiKQogICAgICAgIG9zLiBzeXN0ZW0oImNsZWFyIikKICAgICAgICBvcy4gc3lzdGVtKCJjbGVhciIpCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwpwYXNzcyAoKQpwcmludCAoYisgIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iKQpwcmludCAoIiAgICBXRUxDT01FIFRPIFRISVMgQlkgTTNMT01BVCBUSEUgUEhPTkUgICAgICAiKQpwcmludCAoIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iKQpwcmludCAoIi8gICAgICAgWyArIF0gIFNVUFBPUlQgTUUgT04gWyArIF0gICAgICAgICAgICBcICIpCnByaW50ICgiXCAgaHR0cHM6Ly93d3cueW91dHViZS5jb20vYy9tM2xvbWF0dGhlcGhvbmUgIC8iKQpwcmludCAoIiAgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAiKQpwcmludCAoIiIpCm9zLnN5c3RlbSAoImZpZ2xldCAgIEhJVC1UQiIpCnRpbWUuc2xlZXAoMSkKcHJpbnQgKGYrIiAgKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rIikKdGltZS5zbGVlcCgxKQpwcmludCAoYisiICB8ICBJRCAgfCAgICAgICAgICAgICAgICAgICAgICBOYW1lICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwiKQp0aW1lLnNsZWVwKDEpCnByaW50IChmKyIgICstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKyIpCnRpbWUuc2xlZXAoMSkKcHJpbnQgKGIrIiAgfCBbMDFdIHwgVEhFIE9OQ0UgT0YgT1BFTiBUSElTIFNDUklQVCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8IikKdGltZS5zbGVlcCgxKQpwcmludCAoYisiICB8IFswMl0gfCBUSEUgVFdJQ0UgT1BFTiBUSElTIFNDUklQVCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwiKQp0aW1lLnNsZWVwKDEpCnByaW50IChiKyIgIHwgWzAzXSB8IEVYSVQuLi4gKCArXysgKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfCIpCnRpbWUuc2xlZXAoMSkKcHJpbnQgKGYrIiAgKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rIikKdGltZS5zbGVlcCgxKQpwcmludCAoZisiICAgICAgICAgfCBHTyBUTyA9PT4gaHR0cHM6Ly93d3cueW91dHViZS5jb20vYy9tM2xvbWF0dGhlcGhvbmUgfCIpCnRpbWUuc2xlZXAoMSkKcHJpbnQgKGIrIiAgICAgICAgICArLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKyIpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiAgICAgICAgICAgICAgICAgICAgIyBUSEUgRlJJU1QgU1RBUlQKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKcHJpbnQgKCIiKQpNID0gaW5wdXQgKCJXRUlUIFVSIE9QVElPTlMgVE8gRVhFQ1VURSBJVCA9PT0+ICIpCmlmIE0gPT0gIjEiIDoKICAgbG9nbyAoKQogICBpbXBvcnQgb3MKICAgb3Muc3lzdGVtICgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAteSAmJiBhcHQtZ2V0IHVwZ3JhZGUgLXkgJiBhcHQgdXBkYXRlICIpCiAgIG9zLnN5c3RlbSAoInN1ZG8gYXB0IGluc3RhbGwgYmMiKQogICBvcy5zeXN0ZW0gKCJzdWRvIHJtbW9kIHI4MTg4ZXUua28iKQogICBvcy5zeXN0ZW0gKCJnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL2FpcmNyYWNrLW5nL3J0bDgxODhldXMiKQogICBvcy5zeXN0ZW0gKCJjZCBydGw4MTg4ZXVzIikKICAgb3Muc3lzdGVtICgnZWNobyAiYmxhY2tsaXN0IHI4MTg4ZXUua28iID4gIi9ldGMvbW9kcHJvYmUuZC9yZWFsdGVrLmNvbmYiJykKICAgb3Muc3lzdGVtICgiZXhpdCIpCiAgIG9zLnN5c3RlbSAoInN1ZG8gbWFrZSIpCiAgIG9zLnN5c3RlbSAoInN1ZG8gbWFrZSBpbnN0YWxsIikKICAgb3Muc3lzdGVtICgic3VkbyBtb2Rwcm9iZSA4MTg4ZXUiKQogICBvcy5zeXN0ZW0gKCJzdWRvIGl3IGRldiB3bHhkMDM3NDU3MDc0ZTAgc2V0IHR5cGUgbW9uaXRvciIpCiAgIG9zLnN5c3RlbSAoInN1ZG8gaXcgZGV2IHdsYW4wIHNldCB0eXBlIG1vbml0b3IiKQogICBvcy5zeXN0ZW0gKCJzdWRvIGFpcm1vbi1uZyIpCiMgIG9zLnN5c3RlbSAoInN1ZG8gaXAgbGluayBzZXQgd2xhbjAgZG93biIpCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCmlmIE0gPT0gIjIiIDoKICAgbG9nbyAoKQogICBvcy5zeXN0ZW0gKCJzdWRvIGFwdCBpbnN0YWxsIGJjIikKICAgb3Muc3lzdGVtICgic3VkbyBybW1vZCByODE4OGV1LmtvIikKICAgb3Muc3lzdGVtICgiY2QgcnRsODE4OGV1cyIpCiAgIG9zLnN5c3RlbSAoJ2VjaG8gImJsYWNrbGlzdCByODE4OGV1LmtvIiA+ICIvZXRjL21vZHByb2JlLmQvcmVhbHRlay5jb25mIicpCiAgIG9zLnN5c3RlbSAoImV4aXQiKQogICBvcy5zeXN0ZW0gKCJzdWRvIG1ha2UiKQogICBvcy5zeXN0ZW0gKCJzdWRvIG1ha2UgaW5zdGFsbCIpCiAgIG9zLnN5c3RlbSAoInN1ZG8gbW9kcHJvYmUgODE4OGV1IikKICAgb3Muc3lzdGVtICgic3VkbyBpdyBkZXYgd2x4ZDAzNzQ1NzA3NGUwIHNldCB0eXBlIG1vbml0b3IiKQogICBvcy5zeXN0ZW0gKCJzdWRvIGl3IGRldiB3bGFuMCBzZXQgdHlwZSBtb25pdG9yIikKICAgb3Muc3lzdGVtICgic3VkbyBhaXJtb24tbmciKQojICBvcy5zeXN0ZW0gKCJzdWRvIGlwIGxpbmsgc2V0IHdsYW4wIGRvd24iKQogICAjb3Muc3lzdGVtICgiIikKICAgcHJpbnQgKCJFbm5ubm5kIDBfPj4+ICIpCiAgIHByaW50ICgiZ29vZCIpCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwppZiBNID09ICIzIiA6CiAgIGltcG9ydCBvcwogICBvcy5zeXN0ZW0gKCJleGl0IikKICAgb3Muc3lzdGVtICgiY2QgLi4iKQogICBvcy5zeXN0ZW0gKCJxdWl0IikKICAgb3Muc3lzdGVtICgiZXhpdCIpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMK''' )
exec (base64.b64decode(x))