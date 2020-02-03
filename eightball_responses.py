
async def responses(question: str):

    # default response

    answer = ['Ok, please ask me a real question. I will not be answering otherwise.', 'Ok, do not waste my precious time with your gibberish.', 'Ok, you are absolutely unfunny.', 'Ok, I am a bit iffy on these types of questions. I will therefore not be answering them.']

    # responses

    if question.lower().startswith('should') or question.lower().startswith('can'):

        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, yeah. That sounds good.', 'Ok, no. Although I really do pity you.', 'Ok, but venture only if you dare...', 'Ok, but do not come crying to me when you inevitably regret it.', 'Ok, I cannot believe how unfathomably dense you are. Goodbye.',
                  'Ok. That is a batshit crazy notion, but I am all for it.', 'Ok, but why are you asking me this?', 'Ok, I honestly could not care less about what you want to do.', 'Ok, do whatever you feel you must do. I shall not judge.', 'Ok, the universe has decided so.']

    if question.lower().startswith('am'):

        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, you definitely show the symptoms, so yes.', 'Ok. you do not show the symptoms, fortunately.', 'Ok, the universe has decided so.',
                  'Ok... Rest assured, because you are not.', 'Ok... Rest assured, because you are.', 'Ok... Regardless of what you feel you are, just know that you are loved.', 'Ok, I raise you a better question... Are you stupid?']

    if question.lower().startswith('is') or question.lower().startswith('does') or question.lower().startswith('do i') or question.lower().startswith('do we'):

        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, I can say yes without a doubt.', 'Ok, I can say no without a doubt.', 'Ok... Well, no, unfortunately.', 'Ok... Well, yes, unfortunately.', 'Ok, I raise you a better question... Are you stupid?', 'Ok, the universe has decided so.']

    if question.lower().startswith('if') or question.lower().startswith('will') or question.lower().startswith('would') or question.lower().startswith('could') or question.lower().startswith('shall'):

        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, no. Although I really do pity you.', 'Ok, as I see it, you will. Just be cautious.', 'Ok, with all things considered, yes.', 'Ok, I cannot be certain, but I wish you luck.', 'Ok. Fortunately, no.',
                  'Ok, I do not think I can answer this for you.', 'Ok, I do not think you ever will, and it is not wise to try.', 'Ok, you are better off not doing that. I would like to see you try, though.', 'Ok, the universe has decided so.', 'Ok, do whatever you feel you must do. I shall not judge.']

    # custom responses

    if question.lower().startswith('are you ok') or question.lower().startswith('r u ok') or question.lower().startswith('are u ok') or question.lower().startswith('r you ok') or question.lower().startswith('are you okay'):

        answer = ['I am very OK, and so are you! Thank you for asking.']

    if question.lower().startswith('am i ok') or question.lower().startswith('am i okay'):

        answer = ['Have no doubt. Indeed, you are very OK!']

    return answer
