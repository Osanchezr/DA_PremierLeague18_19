import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_connection(engine):
    """
    Establishes and returns a connection to the database.

    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        The database engine to connect to.

    Returns
    -------
    sqlalchemy.engine.Connection
        A connection to the database.
    """
    return engine.connect()


def most_goals_winner(engine):
    """
    Fetches the team with the most goals scored and checks if it is the winner of the league.

    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        The database engine to connect to.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the team name, points, and total goals scored.
    """
    
    # Query to fetch the team with the most goals scored and check if it is the winner of the league
    consulta1 = """
        SELECT t.common_name,
            (3*t.wins+1*t.draws) as points,
            COALESCE(SUM(CASE WHEN m.id_teams_home = t.id_teams THEN m.home_team_goal_count ELSE 0 END), 0) +
            COALESCE(SUM(CASE WHEN m.id_teams_aways = t.id_teams THEN m.away_team_goal_count ELSE 0 END), 0) AS goals_total
        FROM teams as t
        LEFT JOIN matchs m ON t.id_teams = m.id_teams_home OR t.id_teams = m.id_teams_aways
        GROUP BY t.common_name, t.wins, t.draws
        ORDER BY points DESC;
    """ 

    return pd.read_sql(consulta1, con=engine)

def visualize_most_goals_winner(df):
    """
    Visualizes the team with the most goals scored and checks if it is the winner of the league.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing the team name, points, and total goals scored.

    Returns
    -------
    None
    """
    
    # Establish graphic style whithout grid lines  
    sns.set(style="white")

    # Define figure size
    plt.figure(figsize=(18, 8))

    # Graphip plotting points and goals
    bar_width = 0.35  # Ancho de las barras
    index = range(len(df))  # Índice para cada equipo

    # Graphic points 
    bars1 = plt.bar(index, df['points'], width=bar_width, label='Points', color='#003087')

    # Graphic goals
    bars2 = plt.bar([i + bar_width for i in index], df['goals_total'], width=bar_width, label='Goals', color='#d00027')

    # Add title and labels
    plt.xlabel('Teams', fontsize=14)
    plt.title('Comparison of Points and Goals by Team', fontsize=18)

    # Add teams names as labels on the x-axis
    plt.xticks([i + bar_width / 2 for i in index], df['common_name'], rotation=90, fontsize=12)

    # Add bigger legend
    plt.legend(fontsize=14)

    # Remove y-axis and grid lines
    plt.gca().yaxis.set_visible(False)
    plt.grid(False)

    # Add values to the bars
    for bar in bars1:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=12, color='black')

    for bar in bars2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=12, color='black')

    # Show the graphic
    plt.tight_layout()
    plt.show()


def top_5_goalkeepers(engine):
    """
    Function to retrieve the top 5 goalkeepers of the league.
    
    Parameters
    ----------
    engine : sqlalchemy.engine
        The database connection engine.
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the full name, team name and total goals of the top 5 goalkeepers.
    """
    
    # Query to retrieve the top 5 goalkeepers
    consulta2 = """
        SELECT p.full_name , t.common_name, p.goals_overall
        FROM players as p
        LEFT JOIN teams as t ON p.id_teams = t.id_teams
        ORDER BY goals_overall DESC
        LIMIT 10
    """ 
    # Execute the query and return the results
    return pd.read_sql(consulta2, con=engine)

def visualize_top_5_goalkeepers(df):
    """
    Function to visualize the top 5 goalkeepers of the league.
    
    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing the full name, team name and total goals of the top 5 goalkeepers.
    
    Returns
    -------
    None
    """
    
    # Winner team
    equipo_campeon = "Manchester City"

    # Create a new column to identify the winner team
    df['is_champion_team'] = df['common_name'] == equipo_campeon
    plt.figure(figsize=(12, 8))   
    sns.barplot(x='full_name', y='goals_overall', hue='is_champion_team', data=df, 
                palette={True: '#0057B8', False: '#D50032'}, dodge=False)
    
    # Customize the plot
    plt.xlabel('Player', fontsize=14)
    plt.ylabel('Total Goals', fontsize=14)
    plt.title('Top 10 Scorers: Are they from the Champion Team?', fontsize=18)
    for i, bar in enumerate(plt.gca().patches):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, 
                f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=12, color='black')
    
    plt.xticks(rotation=45, fontsize=12)
    ax = plt.gca()
    ax.set_xticklabels([f'{player}\n({team})' for player, team in zip(df['full_name'], df['common_name'])])
    plt.legend(title='Champion Team', fontsize=12, title_fontsize=14)
    plt.tight_layout()
    plt.show()


def most_possession_wins(engine):
    """
    Function to retrieve the teams with more possession in the field ordered by their average possession.
    
    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        A SQLAlchemy engine to connect to the database.
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the common name, average possession and wins of each team ordered by average possession in descending order.
    """
    
    # Query to retrieve the teams with more possession in the field ordered by their average possession
    consulta3 = """
        SELECT common_name , average_possession, wins
        FROM teams
        ORDER BY average_possession DESC
    """ 
    return pd.read_sql(consulta3, con=engine)

def visualize_most_possession_wins(df):
    """
    Visualizes the relationship between average possession and the number of wins.
    
    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing the common name, average possession and wins of each team ordered by average possession in descending order.
    
    Returns
    -------
    None
    """
    # Set the figure size
    plt.figure(figsize=(12, 8))
    
    # Plot the scatter plot
    sns.scatterplot(x='average_possession', y='wins', hue='common_name', data=df, s=100, palette='Set1', legend=False)
    
    # Plot the regression line
    sns.regplot(x='average_possession', y='wins', data=df, scatter=False, color='black', line_kws={"linestyle":'--', "color":"black"}, ci=None)
    
    # Add the team names on top of the points
    for i in range(df.shape[0]):
        plt.text(df['average_possession'][i] + 0.3, df['wins'][i], df['common_name'][i], 
                fontsize=10, color='black', ha='center', va='bottom')
        
    # Set the labels and title
    plt.xlabel('Average Possession (%)', fontsize=14)
    plt.ylabel('Number of Wins', fontsize=14)
    plt.title('Does Higher Possession Lead to More Wins?', fontsize=18)
    
    # Set the layout to be tight
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    

def stadium_capacity_wins(engine):
    """
    Fetches the number of matches won at home per team ordered by the number of matches won at home in descending order.
    
    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        The database connection engine.
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the common name, stadium name, stadium capacity, and number of matches won at home.
    """
    # Fetch the number of matches won at home per team ordered by the number of matches won at home in descending order
    consulta4 = """
        SELECT t.common_name, s.Stadium, s.ability, COUNT(m.id_match) AS matches_won_at_home
        FROM matchs as m
        # Join the teams table to get the common name of the team
        LEFT JOIN teams as t ON m.id_teams_home = t.id_teams
        # Join the stadiums table to get the stadium name and capacity
        LEFT JOIN stadiums as s ON m.id_stadium = s.id_stadium
        # Filter the matches to only include the matches won at home
        WHERE m.home_team_goal_count > m.away_team_goal_count
        # Group the matches by the common name, stadium name, and stadium capacity
        GROUP BY t.common_name, s.Stadium, s.ability 
        # Order the matches by the number of matches won at home in descending order
        ORDER BY matches_won_at_home DESC
    """ 
    return pd.read_sql(consulta4, con=engine)

def visualize_stadium_capacity_wins(df4):
    """
    Visualizes the relationship between stadium capacity and the number of home wins for each team.
    
    Parameters
    ----------
    df4 : pandas.DataFrame
        A DataFrame containing the common name, stadium name, stadium capacity, and number of matches won at home.
    """
    # Create the figure with a specified size
    plt.figure(figsize=(18, 10))

    # Iterate over each row in the DataFrame
    for i in range(df4.shape[0]):
        # Check if the team is Manchester City or Liverpool
        if df4['common_name'][i] in ['Manchester City', 'Liverpool']:
            # If it is, use the color red
            color = 'red'
        else:
            # If it is not, use the color blue
            color = 'blue'

        # Plot a scatter point with the stadium capacity on the x-axis and the number of home wins on the y-axis
        plt.scatter(df4['ability'][i], df4['matches_won_at_home'][i], color=color, s=100)

    # Plot the regression line
    sns.regplot(x='ability', y='matches_won_at_home', data=df4, scatter=False, color='black', line_kws={"linestyle":'--'}, ci=None)

    # Iterate over each row in the DataFrame again
    for i in range(df4.shape[0]):
        # Check if the team is Manchester City or Liverpool
        color = 'red' if df4['common_name'][i] in ['Manchester City', 'Liverpool'] else 'black'

        # Add a text label with the team name and stadium name
        plt.text(df4['ability'][i] + 300, df4['matches_won_at_home'][i], 
                f"{df4['common_name'][i]}\n{df4['Stadium'][i]}", 
                fontsize=12, color=color, ha='left', va='center')

    # Set the labels and title
    plt.xlabel('Stadium Capacity', fontsize=14)
    plt.ylabel('Home Wins', fontsize=14)
    plt.title('Do Larger Stadiums Lead to More Home Wins?', fontsize=18)

    # Set the layout to be tight
    plt.tight_layout()

    # Show the plot
    plt.show()



def most_sanction_refere(engine):
    """
    Fetches the referee with the most yellow and red cards given during a match
    ordered by the number of yellow and red cards given in descending order.

    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        The database connection engine.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the id_refere, name_refere, total_yellow, total_red, and nro_match.
    """
    # Fetch the referee with the most yellow and red cards given during a match
    # ordered by the number of yellow and red cards given in descending order
    consulta5 = """
        SELECT r.id_refere, r.Name as name_refere, 
               sum(home_team_yellow_cards+away_team_yellow_cards) as total_yellow , 
               sum(home_team_red_cards+away_team_red_cards) as total_red, 
               count(id_match) as nro_match
        FROM matchs m
        LEFT JOIN referes r ON m.id_refere = r.id_refere
        GROUP BY r.id_refere, name_refere
    """ 
    
    return pd.read_sql(consulta5, con=engine)
    

def score_by_team(engine):
    """
    Fetches the score accumulated by teams during a season.

    Parameters
    ----------
    engine : sqlalchemy.engine.Engine
        The database connection engine.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the date, team name, and accumulated score.
    """
    
    # Fetch the score accumulated by teams during a season
    consulta6 = """
        SELECT 
            t2.fecha,
            t2.name_team,
            SUM(t2.points_acum) OVER (PARTITION BY t2.id_teams ORDER BY t2.fecha) AS puntos_acumulados
        FROM (
            SELECT 
                c.date AS fecha,
                t.id_teams,
                t.common_name AS name_team,
                CASE 
                    WHEN (m.id_teams_home = t.id_teams AND m.home_team_goal_count > m.away_team_goal_count) THEN 3  -- Victoria como local
                    WHEN (m.id_teams_aways = t.id_teams AND m.away_team_goal_count > m.home_team_goal_count) THEN 3  -- Victoria como visitante
                    WHEN (m.home_team_goal_count = m.away_team_goal_count) THEN 1  -- Empate
                    ELSE 0  -- Derrota
                END AS points_acum
            FROM teams t
            JOIN matchs m 
                ON t.id_teams = m.id_teams_home 
                OR t.id_teams = m.id_teams_aways
            JOIN calendary c 
                ON m.id_calendary = c.id_calendary
        ) AS t2
        ORDER BY t2.fecha, t2.name_team;
    """ 
    
    return pd.read_sql(consulta6, con=engine)

def visualize_score_by_team(df6):
    """
    This function generates a line plot showing the evolution of the accumulated score by team
    during a season. The x-axis represents the date of the matches, the y-axis represents the
    accumulated score, and the hue of the line represents the team.

    Parameters
    ----------
    df6 : pandas.DataFrame
        A DataFrame containing the date, team name, and accumulated score.

    Returns
    -------
    None
    """
    
    # Convert the 'fecha' column to datetime format
    df6['fecha'] = pd.to_datetime(df6['fecha'])
    
    # Create a line plot with the date on the x-axis, the accumulated score on the y-axis, and
    # the team name as the hue
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df6, x='fecha', y='puntos_acumulados', hue='name_team', marker='o')
    
    # Set the labels and title of the plot
    plt.xlabel('Fecha', fontsize=14)
    plt.ylabel('Puntos Acumulados', fontsize=14)
    plt.title('Evolutivo de Puntos Acumulados por Equipo', fontsize=18)
    
    # Rotate the x-axis tick labels by 45 degrees
    plt.xticks(rotation=45)
    
    # Move the legend to the right side of the plot
    plt.legend(title='Equipos', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    
    # Make sure the plot fits in the figure
    plt.tight_layout()
    
    # Show the plot
    plt.show()



def ratio_of_goals(df):
    df['efficiency_ratio'] = df['goals_per_possession'] / df['goals_per_match']
    df_sorted_efficiency = df.sort_values(by='efficiency_ratio', ascending=False)

    print("Teams ranked by efficiency ratio (goals per possession / goals per match):")
    display(df_sorted_efficiency[['team_name', 'efficiency_ratio']])

def performance_bands(df):
    df['performance_band'] = pd.cut(df['goals_per_match'], bins=[0, 0.02, 0.04, 0.06], labels=['Low', 'Medium', 'High'])
    display(df[['team_name', 'performance_band', 'goals_per_match', 'goals_per_possession']])
   
