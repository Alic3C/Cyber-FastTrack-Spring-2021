# WE01
> 100pt

## Briefing
> View the page at https://cfta-we01.allyourbases.co and try to get the flag.

## Solution
Visiting the site we are presented with the following string:

`ロ='',コ=!ロ+ロ,Y=!コ+ロ,ㅣ=ロ+{},ᗐ=コ[ロ++],Ξ=コ[Δ=ロ],ᐳ=++Δ+ロ,ㅡ=ㅣ[Δ+ᐳ],ウ="+=*:.",コ[ㅡ+=ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+Y[ᐳ]+ᗐ+Ξ+コ[Δ]+ㅡ+ᗐ+ㅣ[ロ]+Ξ][ㅡ](ㅣ[Δ+ᐳ]+ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+Y[ᐳ]+ㅣ[ロ]+Y[Δ]+コ[ᐳ]+ウ[ᐳ+ロ]+Y[Δ]+ㅣ[ロ]+(([]+([]+[])[ㅡ])[ᐳ*(ᐳ+ロ)+Δ])+"(Y[Δ-Δ]+Y[Δ]+Y[ロ]+(([]+([]+[])[ㅡ])[ᐳ*(ᐳ+ロ)+Δ])+ウ[ᐳ]+ㅣ[(ᐳ+ロ)*ロ+ᐳ]+コ[Δ]+(コ.Y+ㅣ)[ロ]+(コ.Y+ㅣ)[ᐳ*Δ-ロ]+ㅡ[ロ-ロ]+ㅡ[ロ]+(コ.Y+ㅣ)[ᐳ-ロ]+コ[ᐳ]+ウ[ロ-ロ]+ㅣ[ロ]+ㅣ[Δ]+Y[Δ-Δ]+コ[Δ]+Y[ᐳ]+ㅡ[ᐳ-ᐳ]+Y[ロ]+ᗐ+(コ.Y+ㅣ)[ᐳ*Δ-ロ]+ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+ウ[ロ]+ㅣ[ᐳ]+Y[ᐳ]+ウ[Δ]+Y[Δ-Δ]+コ[Δ]+(コ.Y+ㅣ)[ロ] )")()`

If we Google the string, it brings us to a [Tweet](https://twitter.com/aemkei/status/755147932081483776) regarding [AUREBESH.js](http://aem1k.com/aurebesh.js/).  

This translates JavaScript to other writing systems!

Running the string in Chrome's developer console gives us the output `flag: unicode+obfuscation=js*fun`.

## Flag
Flag: `unicode+obfuscation=js*fun`
