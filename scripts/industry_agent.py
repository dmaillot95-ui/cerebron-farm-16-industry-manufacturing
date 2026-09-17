import json, os, pathlib
from hf_gradio import GradioClient

role=os.environ['ROLE']; model=os.environ['MODEL']; focus=os.environ['FOCUS']
mission='''CEREBRON OMEGA FARM 16 INDUSTRY MANUFACTURING. Analyze the assigned industrial/manufacturing focus. Separate established engineering facts, assumptions, calculations, simulation proposals, test requirements, risks, unknowns and decisions. Do not fabricate measurements, plant data, standards compliance, supplier capability or experimental results. CLAIM <= EVIDENCE. SIMULATION != TEST. Return a concise technical packet with: findings, calculations_or_checks, failure_modes, validation_tests, unknowns, recommendations.'''
prompt=f"{mission}\nROLE: {role}\nFOCUS: {focus}"
out={'role':role,'model':model,'focus':focus,'inference_success':False,'result':None,'error':None,'epistemic_status':'UNREVIEWED_EXTERNAL_AGENT_OUTPUT'}
try:
    client=GradioClient(model)
    res=client.predict(message=prompt, api_name='/chat')
    out['inference_success']=True; out['result']=res
except Exception as e:
    out['error']=repr(e)
pathlib.Path('out').mkdir(exist_ok=True)
pathlib.Path(f'out/{role}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
