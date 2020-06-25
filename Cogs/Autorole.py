import datetime
import discord
from discord.ext import commands


class Autorole(commands.Cog):
    def __init__(self, client: commands.Bot, member_role_id: int, welcome_channel_id: int):
        self.client: commands.Bot = client
        self.welcome_channel_id: int = welcome_channel_id
        self.member_role: int = member_role_id
        print(f'Addon {self.__class__.__name__} loaded!')

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel: discord.TextChannel = self.client.get_channel(self.welcome_channel_id)
        member_role: discord.Role = member.guild.get_role(self.member_role_id)
        await member.add_roles(self.member_role)
        embed: discord.Embed = discord.Embed(color=discord.Colour(0xdb64f6))
        embed.set_footer(text=f"Ελληνική Κοινότητα Προγραμματιστών | {datetime.datetime.utcnow().strftime('%Y-%m-%d')}")
        embed.set_author(name="Νέο Μέλος!")
        embed.add_field(name=f'Καλώς όρισες {member.mention}!', value="‎")
        embed.set_thumbnail(url=member.avatar_url)
        await welcome_channel.send(embed=embed)


def setup(client: commands.Bot, member_role_id: int, welcome_channel_id: int):
    return client.add_cog(Autorole(client, member_role_id, welcome_channel_id))
