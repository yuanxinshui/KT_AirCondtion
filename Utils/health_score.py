from gmm_hs import gmm_cv_score,GMM_HS
from rule_base import rule_score


def health_result_score(dt,UnitNo,lineNo,trainNo,path_list,CarrageNo='M1',roll_step=30,use_rule=True):
    score=0.0
    if use_rule:
        score=rule_score(UnitNo,dt,lineNo,trainNo)
    
    else:
        database='condition_data'
        sql="select * from " +database+" where HappenTime < '{}' order by HappenTime desc limit 1".format(dt)
        score=gmm_cv_score(sql,UnitNo,lineNo,trainNo,path_list,CarrageNo,roll_step)[0]
    
    return score















if __name__ == "__main__":
    import argparse
    import datetime
    dt= datetime.datetime.now()
    dt_str = datetime.datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')

    parser=argparse.ArgumentParser(description='Train Health AssessMent')
    parser.add_argument('--UnitNo',type=str,default='1#',help='Air Condition Unit Number',choices=['1#','2#'])
    parser.add_argument('--lineNo',type=str,default='5L',help='Subway Line Number')
    parser.add_argument('--trainNo',type=str,default='534',help='Subway Train Number')
    args = parser.parse_args()
    res=rule_score(args.UnitNo,dt_str,args.lineNo,args.trainNo)
    print('{:*^30}'.format('健康评估分数'))  # 使用“*”填充

    print()