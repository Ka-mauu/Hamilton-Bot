import random

from discord.ext import commands

from other.utils import Utils, Emoji


class Eightball(commands.Cog):

    def __init__(self, client):
        self.client = client

    def responses(self, question: str):

        qstn = question.lower()

        # default response

        answer = ['Ok, please ask me a real question. I will not be answering otherwise.', 'Ok, do not waste my precious time with your gibberish.', 'Ok, you are absolutely unfunny.',
                  'Ok, I am a bit iffy on these types of questions. I will therefore not be answering them.', 'Ok, I do not have time to answer these frivolous questions.', 'Ok, that is a meaningless question.', 'Ok, do not bother me with these types of questions.']

        # responses

        if qstn.startswith('should') or qstn.startswith('can'):

            answer = ['Ok, yeah. That sounds good.', 'Ok, no. Although I really do pity you.', 'Ok, but venture only if you dare...', 'Ok, but do not come crying to me when you inevitably regret it.', 'Ok, I cannot believe how unfathomably dense you are. Goodbye.',
                      'Ok. That is a batshit crazy notion, but I am all for it.', 'Ok, but why are you asking me this?', 'Ok, I honestly could not care less about what you want to do.', 'Ok, do whatever you feel you must do. I shall not judge.', 'Ok, the universe has decided so.']

        if qstn.startswith('am'):

            answer = ['Ok, you definitely show the symptoms, so yes.', 'Ok, you do not show the symptoms, fortunately.', 'Ok, the universe has decided so.',
                      'Ok... Rest assured, because you are not.', 'Ok... Rest assured, because you are.', 'Ok... Regardless of what you feel you are, just know that you are loved.', 'Ok, I raise you a better question... Are you stupid?']

        if qstn.startswith('is') or qstn.startswith('does') or qstn.startswith('do i') or qstn.startswith('do we') or qstn.startswith('did') or qstn.startswith('have'):

            answer = ['Ok, I can say yes without a doubt.', 'Ok, I can say no without a doubt.', 'Ok... Well, no, unfortunately.', 'Ok... Well, yes, unfortunately.', 'Ok, I raise you a better question... Are you stupid?',
                      'Ok, the universe has decided so.', 'Ok, I say this with utmost certainty... Yes.', 'Ok, I say this with utmost certainty... No.', 'Ok, I do not think so.', 'Ok, I do believe so.']

        if qstn.startswith('if') or qstn.startswith('will') or qstn.startswith('would') or qstn.startswith('could') or qstn.startswith('shall'):

            answer = ['Ok, no. Although I really do pity you.', 'Ok, as I see it, you will. Just be cautious.', 'Ok, with all things considered, yes.', 'Ok, I cannot be certain, but I wish you luck.', 'Ok. Fortunately, no.',
                      'Ok, I do not think I can answer this for you.', 'Ok, I do not think you ever will, and it is not wise to try.', 'Ok, you are better off not doing that. I would like to see you try, though.', 'Ok, the universe has decided so.', 'Ok, do whatever you feel you must do. I shall not judge.']

        # custom responses

        if qstn.startswith('are you ok') or qstn.startswith('r u ok') or qstn.startswith('are u ok') or qstn.startswith('r you ok') or qstn.startswith('are you okay') or qstn.startswith('r you okay') or qstn.startswith('r u okay') or qstn.startswith('are u okay'):

            answer = ['I am very OK, and so are you! Thank you for asking.']

        if qstn.startswith('am i ok') or qstn.startswith('am i okay') or qstn.startswith('is i okay'):

            answer = ['Have no doubt. Indeed, you are very OK!']

        if qstn.startswith('heads or tails'):

            answer = ['Heads.', 'Tails.']

        if qstn.startswith('am i gay') or qstn.startswith('am i trans') or qstn.startswith('am i transgender') or qstn.startswith('am i bi') or qstn.startswith('am i bisexual') or qstn.startswith('am i straight') or qstn.startswith('am i asexual'):

            answer = ['Ok... Regardless of what you feel you are, just know that you are loved.']

        return answer

    @commands.command(aliases=['8ball', 'ask'], help='Ask Hamilton a yes or no question, and he will respond appropiately.')
    async def eightball(self, ctx, *, question: str):
        answer = self.responses(question)
        await Utils.embed(ctx, f'🔮 What is it that troubles you?', f'{Emoji.hamiltonConfuse} You ask the question, \"**{question.capitalize()}?**\"\n\n{Emoji.hamiltonWisdom} and I answer... \"**{random.choice(answer)}**\"')


def setup(client):
    client.add_cog(Eightball(client))
