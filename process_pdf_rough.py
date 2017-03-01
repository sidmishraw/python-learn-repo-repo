import zlib

encoded_string = b'H‰¬“kPTeÇÏá°ç¬¸"6œ¬sêœ¥S3…Q1´prP¼ ˜2Ù°Ñº¬-,î. ÆEî»ûº¨ˆ°â…ewóÂñ’RD:iƒ¦’¢¢Â¨™–ã¨Måí9ë‹Ñ±üÐôµæ}¿<3ïû~Ï3ÿ?I„†$Ij’t3fO›5F—”<ñi%¿LÊÃCeAó|6®zü(X¢‚×†‚.;ô}æ9"”$éÁsÌ73õs2F½Î’½Òj2fØµ£t£µãââ&j2VSº>K›¤·g2õv¥0kç[ÒMûÊ7´ f³6ùé›6Ù`3XsÿÕ_¨$‰‚D‚J‘H³Ib(5jô˜èqãcb§˜2³ˆŸ`ˆlr0™Dn#y'Äòµº:!ôÓÐSªª»gK4ádqÄ>ô•|G"åX¸ÄÖÕ"÷:n]yµË-`;´©`qçmxªOÜMgÂ*U?¦­•.«-XÆìU­.rºÊ¹Ú,È˜þ*T&:O‹)™^¦vd”»ô<>L?ktVþÍOv?’ÓQA'Ä³&Úå(ù Ô®þ´ÜQšÄO ·ì;zAÝÑÕÖu™'

string = zlib.decompress(encoded_string, 16+zlib.MAX_WBITS)