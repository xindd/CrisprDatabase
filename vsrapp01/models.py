# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AntiAnnotationInfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anticrisprdb_id = models.CharField(db_column='antiCRISPRdb_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprot_entry = models.CharField(db_column='Uniprot entry', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dip = models.CharField(db_column='DIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intact = models.CharField(db_column='IntAct', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genome_region = models.CharField(db_column='Genome_region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locus_tag = models.CharField(db_column='Locus_tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coded_by = models.CharField(max_length=255, blank=True, null=True)
    taxon_id = models.CharField(db_column='Taxon_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anti_annotation_info'


class AntiDna(models.Model):
    id = models.IntegerField(primary_key=True)
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anti_dna'


class AntiHomologTable(models.Model):
    anti_accession = models.CharField(db_column='Anti_Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    homolog_accession = models.CharField(db_column='Homolog_Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_db = models.CharField(db_column='Source DB', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    homolog_def = models.TextField(db_column='Homolog_Def', blank=True, null=True)  # Field name made lowercase.
    evalue = models.CharField(db_column='Evalue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coverage = models.CharField(db_column='Coverage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    query_start = models.CharField(db_column='Query_Start', max_length=255, blank=True, null=True)  # Field name made lowercase.
    query_end = models.CharField(db_column='Query_End', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hit_start = models.CharField(db_column='Hit_Start', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hit_end = models.CharField(db_column='Hit_End', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anticrisprdb_id = models.CharField(db_column='antiCRISPRdb_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anti_homolog_table'


class AntiTable(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crispr_type_inhibited = models.CharField(db_column='CRISPR_type_inhibited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_organism = models.CharField(db_column='Source Organism', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    strategy = models.TextField(db_column='Strategy', blank=True, null=True)  # Field name made lowercase.
    validated = models.CharField(db_column='Validated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.TextField(db_column='Taxonomy', blank=True, null=True)  # Field name made lowercase.
    seq = models.TextField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    size_seq = models.CharField(db_column='Size_seq', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anti_table'


class AnticrisprMechanisms(models.Model):
    id = models.IntegerField(primary_key=True)
    family = models.CharField(db_column='Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    figure = models.CharField(db_column='Figure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    references = models.TextField(db_column='References', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anticrispr_mechanisms'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class VsrMechansim(models.Model):
    id = models.IntegerField(primary_key=True)
    strategy = models.CharField(db_column='Strategy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vsr_id = models.CharField(db_column='VSR_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rnai_inhibited = models.CharField(db_column='RNAi_inhibited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    family_genus = models.CharField(db_column='Family, Genus', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viralzone = models.CharField(db_column='ViralZone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mechanism_of_action = models.TextField(db_column='Mechanism of action', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locus_tag = models.CharField(db_column='Locus_tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    xref_db = models.CharField(db_column='Xref_db', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    structure_pdb_code_field = models.CharField(db_column='Structure (PDB code)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size_aa_field = models.CharField(db_column='Size (aa)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    protein_sequence = models.TextField(db_column='Protein_Sequence', blank=True, null=True)  # Field name made lowercase.
    taxon_id = models.CharField(db_column='Taxon ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tested = models.CharField(db_column='Tested', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vsr_mechansim'


class VsrPicture(models.Model):
    id = models.IntegerField(primary_key=True)
    strategy = models.CharField(db_column='Strategy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    figure = models.CharField(db_column='Figure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    references = models.CharField(db_column='References', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vsr_picture'


class VsrRnaiTable(models.Model):
    rss_id = models.CharField(db_column='RSS_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rnai_inhibited = models.CharField(db_column='RNAi_inhibited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mechanism_of_action = models.TextField(db_column='Mechanism of action', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    family_genus = models.CharField(db_column='Family, Genus', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viralzone = models.CharField(db_column='ViralZone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locus_tag = models.CharField(db_column='Locus_tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    db_xref = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    structure_pdb_code_field = models.CharField(db_column='Structure (PDB code)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size_aa_field = models.CharField(db_column='Size (aa)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    protein_sequence = models.TextField(db_column='Protein_Sequence', blank=True, null=True)  # Field name made lowercase.
    taxon_id = models.CharField(db_column='Taxon ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tested = models.CharField(db_column='Tested', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vsr_rnai_table'


class Knowned30Antidomains(models.Model):
    id = models.IntegerField(primary_key=True)
    proteinid = models.CharField(db_column='ProteinID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genomeid = models.CharField(db_column='GenomeID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_proteinid = models.CharField(db_column='Neighbor_ProteinID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_protein_def = models.TextField(db_column='Neighbor_Protein_Def', blank=True, null=True)  # Field name made lowercase.
    neighbor_protein_location = models.CharField(db_column='Neighbor_Protein_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_domain_id = models.CharField(db_column='Neighbor_Domain_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_domain_name = models.CharField(db_column='Neighbor_Domain_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_domain_def = models.TextField(db_column='Neighbor_Domain_Def', blank=True, null=True)  # Field name made lowercase.
    evalue = models.CharField(max_length=255, blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    coverage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowned30antidomains'


class Jobtable(models.Model):
    jobid = models.IntegerField()
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobtable'


class AntiTable2(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crispr_type_inhibited = models.CharField(db_column='CRISPR_type_inhibited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_organism = models.CharField(db_column='Source Organism', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    strategy = models.TextField(db_column='Strategy', blank=True, null=True)  # Field name made lowercase.
    validated = models.CharField(db_column='Validated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.TextField(db_column='Taxonomy', blank=True, null=True)  # Field name made lowercase.
    seq = models.TextField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    size_seq = models.CharField(db_column='Size_seq', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anti_table_2'


class Knowned30Antidomains2(models.Model):
    id = models.IntegerField(primary_key=True)
    neighbor_proteinid = models.CharField(db_column='Neighbor_ProteinID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anti_accession = models.CharField(db_column='Anti_Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anti_id = models.CharField(db_column='Anti_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    neighbor_def = models.CharField(db_column='Neighbor__Def', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    neighbor_protein_location = models.CharField(db_column='Neighbor_Protein_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'knowned30antidomains2'


class AnticrisprMechanisms2(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    family = models.CharField(db_column='Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    figure = models.CharField(db_column='Figure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    references = models.TextField(db_column='References', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anticrispr_mechanisms2'


class VsrMechansim2(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    strategy = models.CharField(db_column='Strategy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vsr = models.CharField(db_column='VSR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    figure = models.CharField(db_column='Figure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    references = models.CharField(db_column='References', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vsr_mechansim2'


class AntiAnnotationInfo2(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anticrisprdb_id = models.CharField(db_column='antiCRISPRdb_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uniprot_entry = models.CharField(db_column='Uniprot entry', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dip = models.CharField(db_column='DIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intact = models.CharField(db_column='IntAct', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genome_region = models.CharField(db_column='Genome_region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locus_tag = models.CharField(db_column='Locus_tag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coded_by = models.CharField(max_length=255, blank=True, null=True)
    taxon_id = models.CharField(db_column='Taxon_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anti_annotation_info2'
