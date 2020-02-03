def responses(question: str):

    q = question.lower()

    # default response

    answer = ['Ok, please ask me a real question. I will not be answering otherwise.', 'Ok, do not waste my precious time with your gibberish.', 'Ok, you are absolutely unfunny.',
              'Ok, I am a bit iffy on these types of questions. I will therefore not be answering them.', 'Ok, I do not have time to answer these frivolous questions.', 'Ok, that is a meaningless question.', 'Ok, do not bother me with these types of questions.']

    # responses

    if q.startswith('should') or q.startswith('can'):

        answer = ['Ok, yeah. That sounds good.', 'Ok, no. Although I really do pity you.', 'Ok, but venture only if you dare...', 'Ok, but do not come crying to me when you inevitably regret it.', 'Ok, I cannot believe how unfathomably dense you are. Goodbye.',
                  'Ok. That is a batshit crazy notion, but I am all for it.', 'Ok, but why are you asking me this?', 'Ok, I honestly could not care less about what you want to do.', 'Ok, do whatever you feel you must do. I shall not judge.', 'Ok, the universe has decided so.']

    if q.startswith('am'):

        answer = ['Ok, you definitely show the symptoms, so yes.', 'Ok, you do not show the symptoms, fortunately.', 'Ok, the universe has decided so.',
                  'Ok... Rest assured, because you are not.', 'Ok... Rest assured, because you are.', 'Ok... Regardless of what you feel you are, just know that you are loved.', 'Ok, I raise you a better question... Are you stupid?']

    if q.startswith('is') or q.startswith('does') or q.startswith('do i') or q.startswith('do we') or q.startswith('did') or q.startswith('have'):

        answer = ['Ok, I can say yes without a doubt.', 'Ok, I can say no without a doubt.', 'Ok... Well, no, unfortunately.', 'Ok... Well, yes, unfortunately.', 'Ok, I raise you a better question... Are you stupid?',
                  'Ok, the universe has decided so.', 'Ok, I say this with utmost certainty... Yes.', 'Ok, I say this with utmost certainty... No.', 'Ok, I do not think so.', 'Ok, I do believe so.']

    if q.startswith('if') or q.startswith('will') or q.startswith('would') or q.startswith('could') or q.startswith('shall'):

        answer = ['Ok, no. Although I really do pity you.', 'Ok, as I see it, you will. Just be cautious.', 'Ok, with all things considered, yes.', 'Ok, I cannot be certain, but I wish you luck.', 'Ok. Fortunately, no.',
                  'Ok, I do not think I can answer this for you.', 'Ok, I do not think you ever will, and it is not wise to try.', 'Ok, you are better off not doing that. I would like to see you try, though.', 'Ok, the universe has decided so.', 'Ok, do whatever you feel you must do. I shall not judge.']

    # custom responses

    if q.startswith('are you ok') or q.startswith('r u ok') or q.startswith('are u ok') or q.startswith('r you ok') or q.startswith('are you okay') or q.startswith('r you okay') or q.startswith('r u okay') or q.startswith('are u okay'):

        answer = ['I am very OK, and so are you! Thank you for asking.']

    if q.startswith('am i ok') or q.startswith('am i okay') or q.startswith('is i okay'):

        answer = ['Have no doubt. Indeed, you are very OK!']

    return answer
