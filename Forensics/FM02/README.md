# FM02
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](fm02.zip).

- Notice the IRC conversation in stream 57, and read it by following the TCP stream (`tcp.stream eq 57`)
- Observe the discussion of a 7zip file
- We could properly trace the DCC exchange, but it's far simpoler to just search for the hex string `37 7a bc` (the 7zip file header) in all packets.
- Packet #2863 matches, so we follow that stream (`tcp.stream eq 79`)
- Save it out as raw bytes, then convert the hex back to a file, and rename to `.7z`
- The password we need was in the original IRC conversation, base64 encoded, so we can decode it to get the password
  - `TWFyaW9SdWxlejE5ODU=` = `MarioRulez1985`
- We can either `strings` the file we extracted, or just open it in a text editor, to find the flag.

## Flag
Flag: `NESted_in_a_PCAP`
