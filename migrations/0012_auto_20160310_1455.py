# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0011_admin_related_improvements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='email_address',
            field=models.EmailField(blank=True, verbose_name='E-Mail Address', max_length=75, help_text='All outgoing e-mails for this queue will use this e-mail address. If you use IMAP or POP3, this should be the e-mail address for that mailbox.', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='submitter_email',
            field=models.EmailField(blank=True, verbose_name='Submitter E-Mail', max_length=75, help_text='The submitter will receive an email for all public follow-ups left for this task.', null=True),
        ),
        migrations.AlterField(
            model_name='ticketcc',
            name='email',
            field=models.EmailField(blank=True, verbose_name='E-Mail Address', max_length=75, help_text='For non-user followers, enter their e-mail address', null=True),
        ),
    ]
