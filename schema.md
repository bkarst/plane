class Accounts(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    provider_account_id = models.CharField(max_length=255)
    provider = models.CharField()
    access_token = models.TextField()
    access_token_expired_at = models.DateTimeField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    refresh_token_expired_at = models.DateTimeField(blank=True, null=True)
    last_connected_at = models.DateTimeField()
    metadata = models.JSONField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    id_token = models.TextField()

    class Meta:
        managed = False
        db_table = 'accounts'
        unique_together = (('provider', 'provider_account_id'),)


class AnalyticViews(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    query = models.JSONField()
    query_dict = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='analyticviews_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytic_views'


class ApiActivityLogs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    token_identifier = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    query_params = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    response_code = models.IntegerField()
    response_body = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=512, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='apiactivitylogs_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_activity_logs'


class ApiTokens(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    label = models.CharField(max_length=255)
    user_type = models.SmallIntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='apitokens_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='apitokens_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    expired_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    last_used = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_tokens'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Changelogs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    version = models.CharField(max_length=255)
    tags = models.JSONField()
    release_date = models.DateTimeField(blank=True, null=True)
    is_release_candidate = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='changelogs_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changelogs'


class CommentReactions(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    reaction = models.CharField(max_length=20)
    actor = models.ForeignKey('Users', models.DO_NOTHING)
    comment = models.ForeignKey('IssueComments', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='commentreactions_created_by_set', blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='commentreactions_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comment_reactions'
        unique_together = (('comment', 'actor', 'reaction'),)


class CycleFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cycle = models.ForeignKey('Cycles', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='cyclefavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='cyclefavorites_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_favorites'
        unique_together = (('cycle', 'user'),)


class CycleIssues(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cycle = models.ForeignKey('Cycles', models.DO_NOTHING)
    issue = models.OneToOneField('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='cycleissues_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_issues'


class CycleUserProperties(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    filters = models.JSONField()
    display_filters = models.JSONField()
    display_properties = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cycle = models.ForeignKey('Cycles', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='cycleuserproperties_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='cycleuserproperties_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_user_properties'
        unique_together = (('cycle', 'user'),)


class Cycles(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    owned_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='cycles_owned_by_set')
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='cycles_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    view_props = models.JSONField()
    sort_order = models.FloatField()
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)
    progress_snapshot = models.JSONField()
    archived_at = models.DateTimeField(blank=True, null=True)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'cycles'


class DashboardWidgets(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    is_visible = models.BooleanField()
    sort_order = models.FloatField()
    filters = models.JSONField()
    properties = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    dashboard = models.ForeignKey('Dashboards', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='dashboardwidgets_updated_by_set', blank=True, null=True)
    widget = models.ForeignKey('Widgets', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dashboard_widgets'
        unique_together = (('widget', 'dashboard'),)


class Dashboards(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description_html = models.TextField()
    identifier = models.UUIDField(blank=True, null=True)
    is_default = models.BooleanField()
    type_identifier = models.CharField(max_length=30)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    owned_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='dashboards_owned_by_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='dashboards_updated_by_set', blank=True, null=True)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'dashboards'


class DeployBoards(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    entity_identifier = models.UUIDField(blank=True, null=True)
    entity_name = models.CharField(max_length=30)
    anchor = models.CharField(unique=True, max_length=255)
    is_comments_enabled = models.BooleanField()
    is_reactions_enabled = models.BooleanField()
    is_votes_enabled = models.BooleanField()
    view_props = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    inbox = models.ForeignKey('Inboxes', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='deployboards_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'deploy_boards'
        unique_together = (('entity_name', 'entity_identifier'),)


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailNotificationLogs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    entity_identifier = models.UUIDField(blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    data = models.JSONField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    entity = models.CharField(max_length=200)
    old_value = models.CharField(max_length=300, blank=True, null=True)
    new_value = models.CharField(max_length=300, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    receiver = models.ForeignKey('Users', models.DO_NOTHING, related_name='emailnotificationlogs_receiver_set')
    triggered_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='emailnotificationlogs_triggered_by_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='emailnotificationlogs_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_notification_logs'


class EstimatePoints(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    key = models.IntegerField()
    description = models.TextField()
    value = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    estimate = models.ForeignKey('Estimates', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='estimatepoints_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estimate_points'


class Estimates(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='estimates_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    type = models.CharField(max_length=255)
    last_used = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'estimates'
        unique_together = (('name', 'project'),)


class Exporters(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    project = models.TextField(blank=True, null=True)  # This field type is a guess.
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    reason = models.TextField()
    key = models.TextField()
    url = models.CharField(max_length=800, blank=True, null=True)
    token = models.CharField(unique=True, max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    initiated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='exporters_initiated_by_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='exporters_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exporters'


class FileAssets(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    attributes = models.JSONField()
    asset = models.CharField(max_length=100)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='fileassets_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING, blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'file_assets'


class GithubCommentSyncs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    repo_comment_id = models.BigIntegerField()
    comment = models.ForeignKey('IssueComments', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue_sync = models.ForeignKey('GithubIssueSyncs', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='githubcommentsyncs_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_comment_syncs'
        unique_together = (('issue_sync', 'comment'),)


class GithubIssueSyncs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    repo_issue_id = models.BigIntegerField()
    github_issue_id = models.BigIntegerField()
    issue_url = models.CharField(max_length=200)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    repository_sync = models.ForeignKey('GithubRepositorySyncs', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='githubissuesyncs_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_issue_syncs'
        unique_together = (('repository_sync', 'issue'),)


class GithubRepositories(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=200, blank=True, null=True)
    config = models.JSONField()
    repository_id = models.BigIntegerField()
    owner = models.CharField(max_length=500)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='githubrepositories_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_repositories'


class GithubRepositorySyncs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    credentials = models.JSONField()
    actor = models.ForeignKey('Users', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='githubrepositorysyncs_created_by_set', blank=True, null=True)
    label = models.ForeignKey('Labels', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    repository = models.OneToOneField(GithubRepositories, models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='githubrepositorysyncs_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    workspace_integration = models.ForeignKey('WorkspaceIntegrations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_repository_syncs'
        unique_together = (('project', 'repository'),)


class GlobalViews(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    query = models.JSONField()
    access = models.SmallIntegerField()
    query_data = models.JSONField()
    sort_order = models.FloatField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='globalviews_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'global_views'


class Importers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    service = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    metadata = models.JSONField()
    config = models.JSONField()
    data = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    initiated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='importers_initiated_by_set')
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    token = models.ForeignKey(ApiTokens, models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='importers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    imported_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importers'


class InboxIssues(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    status = models.IntegerField()
    snoozed_till = models.DateTimeField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    duplicate_to = models.ForeignKey('Issues', models.DO_NOTHING, blank=True, null=True)
    inbox = models.ForeignKey('Inboxes', models.DO_NOTHING)
    issue = models.ForeignKey('Issues', models.DO_NOTHING, related_name='inboxissues_issue_set')
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='inboxissues_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inbox_issues'


class Inboxes(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_default = models.BooleanField()
    view_props = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='inboxes_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'inboxes'
        unique_together = (('name', 'project'),)


class InstanceAdmins(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    role = models.IntegerField()
    is_verified = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    instance = models.ForeignKey('Instances', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='instanceadmins_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='instanceadmins_user_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_admins'
        unique_together = (('instance', 'user'),)


class InstanceConfigurations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    key = models.CharField(unique=True, max_length=100)
    value = models.TextField(blank=True, null=True)
    category = models.TextField()
    is_encrypted = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='instanceconfigurations_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_configurations'


class Instances(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    instance_name = models.CharField(max_length=255)
    whitelist_emails = models.TextField(blank=True, null=True)
    instance_id = models.CharField(unique=True, max_length=255)
    license_key = models.CharField(max_length=256, blank=True, null=True)
    current_version = models.CharField(max_length=255)
    last_checked_at = models.DateTimeField()
    namespace = models.CharField(max_length=255, blank=True, null=True)
    is_telemetry_enabled = models.BooleanField()
    is_support_required = models.BooleanField()
    is_setup_done = models.BooleanField()
    is_signup_screen_visited = models.BooleanField()
    user_count = models.BigIntegerField()
    is_verified = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='instances_updated_by_set', blank=True, null=True)
    domain = models.TextField()
    latest_version = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'instances'


class Integrations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=400)
    provider = models.CharField(unique=True, max_length=400)
    network = models.IntegerField()
    description = models.JSONField()
    author = models.CharField(max_length=400)
    webhook_url = models.TextField()
    webhook_secret = models.TextField()
    redirect_url = models.TextField()
    metadata = models.JSONField()
    verified = models.BooleanField()
    avatar_url = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='integrations_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integrations'


class IssueActivities(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    verb = models.CharField(max_length=255)
    field = models.CharField(max_length=255, blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    comment = models.TextField()
    attachments = models.TextField()  # This field type is a guess.
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING, blank=True, null=True)
    issue_comment = models.ForeignKey('IssueComments', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueactivities_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    actor = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueactivities_actor_set', blank=True, null=True)
    new_identifier = models.UUIDField(blank=True, null=True)
    old_identifier = models.UUIDField(blank=True, null=True)
    epoch = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_activities'


class IssueAssignees(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    assignee = models.ForeignKey('Users', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueassignees_created_by_set', blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueassignees_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_assignees'
        unique_together = (('issue', 'assignee'),)


class IssueAttachments(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    attributes = models.JSONField()
    asset = models.CharField(max_length=100)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueattachments_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_attachments'


class IssueBlockers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    block = models.ForeignKey('Issues', models.DO_NOTHING)
    blocked_by = models.ForeignKey('Issues', models.DO_NOTHING, related_name='issueblockers_blocked_by_set')
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueblockers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_blockers'


class IssueComments(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    comment_stripped = models.TextField()
    attachments = models.TextField()  # This field type is a guess.
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuecomments_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    actor = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuecomments_actor_set', blank=True, null=True)
    comment_html = models.TextField()
    comment_json = models.JSONField()
    access = models.CharField(max_length=100)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_comments'


class IssueLabels(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    label = models.ForeignKey('Labels', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuelabels_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_labels'


class IssueLinks(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuelinks_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    metadata = models.JSONField()

    class Meta:
        managed = False
        db_table = 'issue_links'


class IssueMentions(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    mention = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuementions_mention_set')
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuementions_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_mentions'
        unique_together = (('issue', 'mention'),)


class IssueProperties(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    display_properties = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueproperties_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueproperties_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    display_filters = models.JSONField()
    filters = models.JSONField()

    class Meta:
        managed = False
        db_table = 'issue_properties'
        unique_together = (('user', 'project'),)


class IssueReactions(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    reaction = models.CharField(max_length=20)
    actor = models.ForeignKey('Users', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuereactions_created_by_set', blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuereactions_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_reactions'
        unique_together = (('issue', 'actor', 'reaction'),)


class IssueRelations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    relation_type = models.CharField(max_length=20)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    related_issue = models.ForeignKey('Issues', models.DO_NOTHING, related_name='issuerelations_related_issue_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuerelations_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_relations'
        unique_together = (('issue', 'related_issue'),)


class IssueSequences(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    sequence = models.BigIntegerField()
    deleted = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuesequences_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_sequences'


class IssueSubscribers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    subscriber = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuesubscribers_subscriber_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuesubscribers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_subscribers'
        unique_together = (('issue', 'subscriber'),)


class IssueViews(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    query = models.JSONField()
    access = models.SmallIntegerField()
    filters = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueviews_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    display_filters = models.JSONField()
    display_properties = models.JSONField()
    sort_order = models.FloatField()
    logo_props = models.JSONField()
    is_locked = models.BooleanField()
    owned_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issueviews_owned_by_set')

    class Meta:
        managed = False
        db_table = 'issue_views'


class IssueVotes(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    vote = models.IntegerField()
    actor = models.ForeignKey('Users', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuevotes_created_by_set', blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issuevotes_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_votes'
        unique_together = (('issue', 'actor'),)


class Issues(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.JSONField()
    priority = models.CharField(max_length=30)
    start_date = models.DateField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    sequence_id = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    state = models.ForeignKey('States', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='issues_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    description_html = models.TextField()
    description_stripped = models.TextField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    sort_order = models.FloatField()
    point = models.IntegerField(blank=True, null=True)
    archived_at = models.DateField(blank=True, null=True)
    is_draft = models.BooleanField()
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)
    description_binary = models.BinaryField(blank=True, null=True)
    estimate_point = models.ForeignKey(EstimatePoints, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class Labels(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='labels_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    color = models.CharField(max_length=255)
    sort_order = models.FloatField()
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labels'
        unique_together = (('name', 'project'),)


class ModuleFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='modulefavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='modulefavorites_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_favorites'
        unique_together = (('module', 'user'),)


class ModuleIssues(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey(Issues, models.DO_NOTHING)
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='moduleissues_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_issues'
        unique_together = (('issue', 'module'),)


class ModuleLinks(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=200)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='modulelinks_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    metadata = models.JSONField()

    class Meta:
        managed = False
        db_table = 'module_links'


class ModuleMembers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey('Users', models.DO_NOTHING, related_name='modulemembers_member_set')
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='modulemembers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_members'
        unique_together = (('module', 'member'),)


class ModuleUserProperties(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    filters = models.JSONField()
    display_filters = models.JSONField()
    display_properties = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='moduleuserproperties_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='moduleuserproperties_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_user_properties'
        unique_together = (('module', 'user'),)


class Modules(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_text = models.JSONField(blank=True, null=True)
    description_html = models.JSONField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey('Users', models.DO_NOTHING, related_name='modules_lead_set', blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='modules_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    view_props = models.JSONField()
    sort_order = models.FloatField()
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'modules'
        unique_together = (('name', 'project'),)


class Notifications(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    data = models.JSONField(blank=True, null=True)
    entity_identifier = models.UUIDField(blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    title = models.TextField()
    message = models.JSONField(blank=True, null=True)
    message_html = models.TextField()
    message_stripped = models.TextField(blank=True, null=True)
    sender = models.CharField(max_length=255)
    read_at = models.DateTimeField(blank=True, null=True)
    snoozed_till = models.DateTimeField(blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    receiver = models.ForeignKey('Users', models.DO_NOTHING, related_name='notifications_receiver_set')
    triggered_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='notifications_triggered_by_set', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='notifications_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications'


class PageBlocks(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.JSONField()
    description_html = models.TextField()
    description_stripped = models.TextField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    issue = models.ForeignKey(Issues, models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pageblocks_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    sort_order = models.FloatField()
    sync = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'page_blocks'


class PageFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pagefavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='pagefavorites_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'page_favorites'
        unique_together = (('page', 'user'),)


class PageLabels(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    label = models.ForeignKey(Labels, models.DO_NOTHING)
    page = models.ForeignKey('Pages', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pagelabels_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'page_labels'


class PageLogs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    transaction = models.UUIDField()
    entity_identifier = models.UUIDField(blank=True, null=True)
    entity_name = models.CharField(max_length=30)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pagelogs_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'page_logs'
        unique_together = (('page', 'transaction'),)


class Pages(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.JSONField()
    description_html = models.TextField()
    description_stripped = models.TextField(blank=True, null=True)
    access = models.SmallIntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    owned_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pages_owned_by_set')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pages_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    color = models.CharField(max_length=255)
    archived_at = models.DateField(blank=True, null=True)
    is_locked = models.BooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    view_props = models.JSONField()
    logo_props = models.JSONField()
    description_binary = models.BinaryField(blank=True, null=True)
    is_global = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pages'


class Profiles(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    theme = models.JSONField()
    is_tour_completed = models.BooleanField()
    onboarding_step = models.JSONField()
    use_case = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=300, blank=True, null=True)
    is_onboarded = models.BooleanField()
    last_workspace_id = models.UUIDField(blank=True, null=True)
    billing_address_country = models.CharField(max_length=255)
    billing_address = models.JSONField(blank=True, null=True)
    has_billing_address = models.BooleanField()
    company_name = models.CharField(max_length=255)
    user = models.OneToOneField('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profiles'


class ProjectDeployBoards(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    anchor = models.CharField(unique=True, max_length=255)
    comments = models.BooleanField()
    reactions = models.BooleanField()
    votes = models.BooleanField()
    views = models.JSONField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    inbox = models.ForeignKey(Inboxes, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectdeployboards_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_deploy_boards'
        unique_together = (('project', 'anchor'),)


class ProjectFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectfavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectfavorites_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_favorites'
        unique_together = (('project', 'user'),)


class ProjectIdentifiers(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=12)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.OneToOneField('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectidentifiers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_identifiers'
        unique_together = (('name', 'workspace'),)


class ProjectMemberInvites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=255)
    accepted = models.BooleanField()
    token = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    responded_at = models.DateTimeField(blank=True, null=True)
    role = models.SmallIntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectmemberinvites_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_member_invites'


class ProjectMembers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    role = models.SmallIntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectmembers_member_set', blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectmembers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    view_props = models.JSONField()
    default_props = models.JSONField()
    sort_order = models.FloatField()
    preferences = models.JSONField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'project_members'
        unique_together = (('project', 'member'),)


class ProjectPages(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(Pages, models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectpages_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_pages'
        unique_together = (('project', 'page'),)


class ProjectPublicMembers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectpublicmembers_member_set')
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projectpublicmembers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_public_members'
        unique_together = (('project', 'member'),)


class Projects(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_text = models.JSONField(blank=True, null=True)
    description_html = models.JSONField(blank=True, null=True)
    network = models.SmallIntegerField()
    identifier = models.CharField(max_length=12)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    default_assignee = models.ForeignKey('Users', models.DO_NOTHING, related_name='projects_default_assignee_set', blank=True, null=True)
    project_lead = models.ForeignKey('Users', models.DO_NOTHING, related_name='projects_project_lead_set', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='projects_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    emoji = models.CharField(max_length=255, blank=True, null=True)
    cycle_view = models.BooleanField()
    module_view = models.BooleanField()
    cover_image = models.CharField(max_length=800, blank=True, null=True)
    issue_views_view = models.BooleanField()
    page_view = models.BooleanField()
    estimate = models.ForeignKey(Estimates, models.DO_NOTHING, blank=True, null=True)
    icon_prop = models.JSONField(blank=True, null=True)
    inbox_view = models.BooleanField()
    archive_in = models.IntegerField()
    close_in = models.IntegerField()
    default_state = models.ForeignKey('States', models.DO_NOTHING, blank=True, null=True)
    logo_props = models.JSONField()
    archived_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'
        unique_together = (('identifier', 'workspace'), ('name', 'workspace'),)


class Sessions(models.Model):
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    device_info = models.JSONField(blank=True, null=True)
    session_key = models.CharField(primary_key=True, max_length=128)
    user_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class SlackProjectSyncs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    access_token = models.CharField(max_length=300)
    scopes = models.TextField()
    bot_user_id = models.CharField(max_length=50)
    webhook_url = models.CharField(max_length=1000)
    data = models.JSONField()
    team_id = models.CharField(max_length=30)
    team_name = models.CharField(max_length=300)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='slackprojectsyncs_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    workspace_integration = models.ForeignKey('WorkspaceIntegrations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'slack_project_syncs'
        unique_together = (('team_id', 'project'),)


class SocialLoginConnections(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    medium = models.CharField(max_length=20)
    last_login_at = models.DateTimeField(blank=True, null=True)
    last_received_at = models.DateTimeField(blank=True, null=True)
    token_data = models.JSONField(blank=True, null=True)
    extra_data = models.JSONField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='socialloginconnections_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='socialloginconnections_user_set')

    class Meta:
        managed = False
        db_table = 'social_login_connections'


class States(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='states_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    sequence = models.FloatField()
    group = models.CharField(max_length=20)
    default = models.BooleanField()
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_source = models.CharField(max_length=255, blank=True, null=True)
    is_triage = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'states'
        unique_together = (('name', 'project'),)


class TeamMembers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey('Users', models.DO_NOTHING, related_name='teammembers_member_set')
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='teammembers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_members'
        unique_together = (('team', 'member'),)


class TeamPages(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(Pages, models.DO_NOTHING)
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='teampages_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_pages'
        unique_together = (('team', 'page'),)


class Teams(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='teams_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'teams'
        unique_together = (('name', 'workspace'),)


class UserFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    entity_type = models.CharField(max_length=100)
    entity_identifier = models.UUIDField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_folder = models.BooleanField()
    sequence = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='userfavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='userfavorites_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_favorites'
        unique_together = (('entity_type', 'user', 'entity_identifier'),)


class UserNotificationPreferences(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    property_change = models.BooleanField()
    state_change = models.BooleanField()
    comment = models.BooleanField()
    mention = models.BooleanField()
    issue_completed = models.BooleanField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='usernotificationpreferences_updated_by_set', blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name='usernotificationpreferences_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_notification_preferences'


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    username = models.CharField(unique=True, max_length=128)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.TextField()
    date_joined = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_location = models.CharField(max_length=255)
    created_location = models.CharField(max_length=255)
    is_superuser = models.BooleanField()
    is_managed = models.BooleanField()
    is_password_expired = models.BooleanField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_email_verified = models.BooleanField()
    is_password_autoset = models.BooleanField()
    token = models.CharField(max_length=64)
    user_timezone = models.CharField(max_length=255)
    last_active = models.DateTimeField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    last_logout_time = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=255)
    last_logout_ip = models.CharField(max_length=255)
    last_login_medium = models.CharField(max_length=20)
    last_login_uagent = models.TextField()
    token_updated_at = models.DateTimeField(blank=True, null=True)
    is_bot = models.BooleanField()
    cover_image = models.CharField(max_length=800, blank=True, null=True)
    display_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('user', 'group'),)


class UsersUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_permissions'
        unique_together = (('user', 'permission'),)


class ViewFavorites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='viewfavorites_updated_by_set', blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, related_name='viewfavorites_user_set')
    view = models.ForeignKey(IssueViews, models.DO_NOTHING)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'view_favorites'
        unique_together = (('view', 'user'),)


class WebhookLogs(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    event_type = models.CharField(max_length=255, blank=True, null=True)
    request_method = models.CharField(max_length=10, blank=True, null=True)
    request_headers = models.TextField(blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response_status = models.TextField(blank=True, null=True)
    response_headers = models.TextField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    retry_count = models.SmallIntegerField()
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='webhooklogs_updated_by_set', blank=True, null=True)
    webhook = models.ForeignKey('Webhooks', models.DO_NOTHING)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'webhook_logs'


class Webhooks(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    url = models.CharField(max_length=200)
    is_active = models.BooleanField()
    secret_key = models.CharField(max_length=255)
    project = models.BooleanField()
    issue = models.BooleanField()
    module = models.BooleanField()
    cycle = models.BooleanField()
    issue_comment = models.BooleanField()
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='webhooks_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'webhooks'
        unique_together = (('workspace', 'url'),)


class Widgets(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    key = models.CharField(max_length=255)
    filters = models.JSONField()
    logo_props = models.JSONField()

    class Meta:
        managed = False
        db_table = 'widgets'


class WorkspaceIntegrations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    metadata = models.JSONField()
    config = models.JSONField()
    actor = models.ForeignKey(Users, models.DO_NOTHING)
    api_token = models.ForeignKey(ApiTokens, models.DO_NOTHING)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaceintegrations_created_by_set', blank=True, null=True)
    integration = models.ForeignKey(Integrations, models.DO_NOTHING)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaceintegrations_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_integrations'
        unique_together = (('workspace', 'integration'),)


class WorkspaceMemberInvites(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=255)
    accepted = models.BooleanField()
    token = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    responded_at = models.DateTimeField(blank=True, null=True)
    role = models.SmallIntegerField()
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspacememberinvites_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_member_invites'
        unique_together = (('email', 'workspace'),)


class WorkspaceMembers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    role = models.SmallIntegerField()
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspacemembers_member_set')
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspacemembers_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)
    company_role = models.TextField(blank=True, null=True)
    view_props = models.JSONField()
    default_props = models.JSONField()
    issue_props = models.JSONField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'workspace_members'
        unique_together = (('workspace', 'member'),)


class WorkspaceThemes(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    colors = models.JSONField()
    actor = models.ForeignKey(Users, models.DO_NOTHING)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspacethemes_created_by_set', blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspacethemes_updated_by_set', blank=True, null=True)
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_themes'
        unique_together = (('workspace', 'name'),)


class WorkspaceUserProperties(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    filters = models.JSONField()
    display_filters = models.JSONField()
    display_properties = models.JSONField()
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaceuserproperties_updated_by_set', blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaceuserproperties_user_set')
    workspace = models.ForeignKey('Workspaces', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_user_properties'
        unique_together = (('workspace', 'user'),)


class Workspaces(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=80)
    logo = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=48)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaces_owner_set')
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, related_name='workspaces_updated_by_set', blank=True, null=True)
    organization_size = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workspaces'

Given the above schema, how do I get all the assignees assigned to an issue in django?