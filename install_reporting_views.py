#!/usr/bin/python
import jinja2
import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--tenant', help='The tenant Id')
parser.add_argument('--schema', help='Name for the reporting schema')
parser.add_argument('--user', help='Define a limited-access user for the reporting schema')
parser.add_argument('--pw', help='Set the limited-access user password')

args=parser.parse_args()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
VIEWS_TEMPLATE = "reporting_views.sql.jinja"
template = templateEnv.get_template(VIEWS_TEMPLATE)

outputText = template.render(tenantId=args.tenant, schema_name=args.schema)  # this is where to put args to the template renderer

if (args.user):
  USER_TEMPLATE = "reporting_user.sql.jinja"
  template = templateEnv.get_template(USER_TEMPLATE)
  outputText += template.render(tenantId=args.tenant,schema_name=args.schema,user=args.user,pw=args.pw)

print(outputText)
