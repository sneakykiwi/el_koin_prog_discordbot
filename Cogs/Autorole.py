from discord.ext import commands
import discord, datetime

class Autorole(commands.Cog):
    def __init__(self, client: commands.Bot, guild_id: int, member_role_id: int, welcome_channel_id: int):
        self.client: commands.Bot = client
        self.guild: discord.Guild = self.client.get_guild(guild_id)
        self.welcome_channel: discord.TextChannel = self.client.get_channel(welcome_channel_id)
        self.member_role: discord.Role = self.guild.get_role(member_role_id)
        print(f'Addon {self.__class__.__name__} loaded!')


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.add_roles(self.member_role)
        embed: discord.Embed = discord.Embed(color=discord.Colour(0xdb64f6))
        embed.set_footer(text=f"Ελληνική Κοινότητα Προγραμματιστών | {datetime.datetime.utcnow().strftime('%Y-%m-%d'}")
        embed.set_author(name="Νέο Μέλος!")
        embed.add_field(name=f'Καλώς όρισες {member.mention}!', value="‎")
        embed.set_thumbnail(url=member.avatar_url)
        await self.welcome_channel.send(embed=embed)


def setup(client: commands.Bot, guild_id: int, member_role_id: int, welcome_channel_id: int):
    return client.add_cog(Autorole(client, guild_id, member_role_id, welcome_channel_id))
