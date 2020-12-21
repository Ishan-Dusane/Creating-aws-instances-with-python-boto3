# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:22:09 2020

@author: mithi
"""

import sys
import boto3

# Terminate specific instance
def terminate_instance():
    ec2 = boto3.resource('ec2',region_name='us-east-1',
    aws_access_key_id='AKIAJ7LNKN4RPGCTSBPQ',
    aws_secret_access_key='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')
    for instance_id_i in sys.argv[1:]:
        instance = ec2.Instance(instance_id_i)
        response = instance.terminate()
        print("shutting down instance..termination in progress")
        instance.wait_until_terminated()
        print("\nInstance Terminated:\n",response)

# List all instances
def list_instances():
    ec2 = boto3.resource('ec2',region_name='us-east-1',
    aws_access_key_id='AKIAJ7LNKN4RPGCTSBPQ',
    aws_secret_access_key='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')
    for instance in ec2.instances.all():
        print("\nInstance ID : ",instance.id, "\nState : ", instance.state,"\nLocation : ", instance.placement['AvailabilityZone'], "\nIP : ", instance.public_ip_address)

if __name__ == '__main__':
    terminate_instance()
    list_instances()