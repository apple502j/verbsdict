'''
English Verbs database
Licensed under BSD 2-clause,MIT,and cc by all ver.

Copyright (C) 2017 apple502j
All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, are permitted provided
that the following conditions are met:

	1 Redistributions of source code must retain
	the above copyright notice, this list of
	conditions and the following disclaimer.
	
	2 Redistributions in binary form must reproduce
	the above copyright notice, this list of conditions
	and the following disclaimer in the documentation
	and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 


Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE. 

https://creativecommons.org/licenses/by/1.0/
https://creativecommons.org/licenses/by/2.0/
https://creativecommons.org/licenses/by/2.5/
https://creativecommons.org/licenses/by/3.0/
https://creativecommons.org/licenses/by/4.0/

'''

verbsDict = {
"be"	:	"^((a|we)re|(i|wa)s|am|be(|en))$",
"become"	:	"^bec(omes?|ame)$",
"begin"	:	"^beg(ins?|an|un)$",
"break"	:	"^bre(aks?|oken?)$",
"bring"	:	"^br(ings?|ought)$",
"build"	:	"^buil(ds?|t)$",
"buy"	:	"^b(uys?|ought)$",
"catch"	:	"^ca(tch(|es)|ught)$",
"come"	:	"^c(omes?|ame)$",
"cut"	:	"^cuts?$",
"do"	:	"^d(o(|es|ne)|id)$",
"read"	:	"^reads?$",
"drink"	:	"^dr(inks?|(a|u)nk)$",
"feel"	:	"^fe(els?|lt)$",
"eat"	:	"^(eat(|s|en)|ate)$",
"find"	:	"^f(inds?|ound)$",
"forget"	:	"forg(ets?|ot(|ten))$",
"give"	:	"^g(ive(|s|n)|ave)$",
"go"	:	"^(went|go(|es|ne))$",
"grow"	:	"^gr(ow(|s|n)|ew)$",
"have"	:	"^ha(ve|s|d)$",
"hear"	:	"^hear(|s|d)$",
"hold"	:	"^h(olds?|eld)$",
"keep"	:	"^ke(eps?|pt)$",
"know"	:	"^kn(ow(|s|n)|ew)$",
"leave"	:	"^le(aves?|ft)$",
"make"	:	"^ma(kes?|de)$",
"mean"	:	"^mean(|s|t)$",
"meet"	:	"^me(ets?|t)$",
"pay"	:	"^pa(ys?|id)$",
"put"	:	"^puts?$",
"run"	:	"^r(uns?|an)$",
"say"	:	"^sa(ys?|id)$",
"see"	:	"^s(ee(|s|n)|aw)$",
"sell"	:	"^s(ells?|old)$",
"send"	:	"^sen(ds?|t)$",
"show"	:	"^show(|s|n|ed)$",
"sing"	:	"^s(ings?|(a|u)ng)$",
"sit"	:	"^s(its?|at)$",
"sleep"	:	"^sle(eps?|pt)$",
"speak"	:	"^sp(eaks?|oken?)$",
"stand"	:	"^st(ands?|ood)$",
"swim"	:	"^sw(ims?|(a|u)m)$",
"take"	:	"^t(ake(|s|n)|ook)$",
"teach"	:	"^t(each(|es)|aught)$",
"tell"	:	"^t(ells?|old)$",
"think"	:	"^th(inks?|ought)$",
"throw"	:	"^thr(ow(|s|n)|ew)$",
"understand"	:	"^underst(ands?|ood)$",
"write"	:	"^wr(it(es?|ten)|ote)$",
"drive"	:	"^dr(ive(|s|n)|ove)$",
"fly"	:	"^fl(y|ies|ew|own)$",
"fall"	:	"^f(all(|s|en)|ell)$",
"choose"	:	"^ch(ooses?|osen?)$",
"lose"	:	"^los(es?|t)$",
"spend"	:	"^spen(ds?|t)$",
"wake"	:	"^w(akes?|oken?)$",
"wear"	:	"^w(ears?|or(e|n))$",
"win"	:	"^w(ins?|on)$",
"let"	:	"^lets?$",
"hit"	:	"^hits?$",
"hurt"	:	"^hurts?$"
}

