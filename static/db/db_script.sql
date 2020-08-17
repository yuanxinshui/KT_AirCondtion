/*
Navicat MySQL Data Transfer

Source Server         : mysql56
Source Server Version : 50618
Source Host           : localhost:3306
Source Database       : air_condition

Target Server Type    : MYSQL
Target Server Version : 50618
File Encoding         : 65001

Date: 2020-07-23 09:51:30
*/

SET FOREIGN_KEY_CHECKS=0;


-- ----------------------------
-- Table structure for condition_data
-- ----------------------------
DROP TABLE IF EXISTS `condition_data`;
CREATE TABLE `condition_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Metro_Line_No` varchar(255) DEFAULT NULL,
  `Train_Type` varchar(255) DEFAULT NULL,
  `TrainNo` varchar(11) DEFAULT NULL,
  `CarriageNo` varchar(255) DEFAULT NULL,
  `UnitNo` varchar(255) DEFAULT NULL,
  `HappenTime` datetime DEFAULT NULL,
  `ReturnTemper_1` float DEFAULT NULL,
  `ReturnTemper_2` float(255,0) DEFAULT NULL,
  `VentilationTemper_1` float(255,0) DEFAULT NULL,
  `VentilationTemper_2` float DEFAULT NULL,
  `DeliveryTemper_1` float NOT NULL,
  `DeliveryTemper_2` float DEFAULT NULL,
  `Sys1_Evaporator1_MedTemper` float(255,0) DEFAULT NULL,
  `Sys1_Evaporator2_MedTemper` float DEFAULT NULL,
  `Sys2_Evaporator1_MedTemper` float DEFAULT NULL,
  `Sys2_Evaporator2_MedTemper` float DEFAULT NULL,
  `Evaporator1_OutletTemper_1` float DEFAULT NULL,
  `Evaporator1_OutletTemper_2` float DEFAULT NULL,
  `Evaporator2_OutletTemper_1` float DEFAULT NULL,
  `Evaporator2_OutletTemper_2` float DEFAULT NULL,
  `Condenser1_Temper` float DEFAULT NULL,
  `Condenser2_Temper` float DEFAULT NULL,
  `Sys1_InspiratoryTemper` float(255,0) DEFAULT NULL,
  `Sys2_InspiratoryTemper` float(255,0) DEFAULT NULL,
  `Sys1_ExhaustTemper` float DEFAULT NULL,
  `Sys2_ExhaustTemper` float DEFAULT NULL,
  `Sys1_LowPressure` float DEFAULT NULL,
  `Sys2_LowPressure` float(255,0) DEFAULT NULL,
  `Sys1_HighPressure` float(255,0) DEFAULT NULL,
  `Sys2_HighPressure` float DEFAULT NULL,
  `Sys1_CondensPressure` float DEFAULT NULL,
  `Sys2_CondensPressure` float DEFAULT NULL,
  `Passenger_CompartTempter_1` float DEFAULT NULL,
  `Passenger_CompartTempter_2` float(255,0) DEFAULT NULL,
  `Passenger_HumidityTempter_1` float DEFAULT NULL,
  `Passenger_HumidityTempter_2` float(255,0) DEFAULT NULL,
  `UnitTempter_1` float(255,0) DEFAULT NULL,
  `UnitTempter_2` float DEFAULT NULL,
  `UnitHumidity_1` float DEFAULT NULL,
  `UnitHumidity_2` float(255,0) DEFAULT NULL,
  `FreshValve_FB_1` float DEFAULT NULL,
  `FreshValve_FB_2` float DEFAULT NULL,
  `L1_L2_V` float DEFAULT NULL,
  `L3_L2_V` float DEFAULT NULL,
  `L1_L3_V` float DEFAULT NULL,
  `L1_Current` float DEFAULT NULL,
  `L2_Current` float DEFAULT NULL,
  `L3_Current` float DEFAULT NULL,
  `N_Current` float DEFAULT NULL,
  `Energy_H` float DEFAULT NULL,
  `Energy_L` float DEFAULT NULL,
  `PowerRate_H` float DEFAULT NULL,
  `PowerRate_L` float DEFAULT NULL,
  `Unit_Mean_V` float DEFAULT NULL,
  `Unit_Mean_Current` float(255,0) DEFAULT NULL,
  `Sys1_Discharge_Superheat` float DEFAULT NULL,
  `Sys2_Discharge_Superheat` float(255,0) DEFAULT NULL,
  `Sys1_Inspiratory_Superheat` float DEFAULT NULL,
  `Sys2_Inspiratory_Superheat` float DEFAULT NULL,
  `Sys1_Condens_Undercool` float DEFAULT NULL,
  `Sys2_Condens_Undercool` float DEFAULT NULL,
  `Sys1_EvaporSat_Tempter` float(255,0) DEFAULT NULL,
  `Sys2_EvaporSat_Tempter` float(255,0) DEFAULT NULL,
  `Sys1_CondensSat_Tempter` float(255,0) DEFAULT NULL,
  `Sys2_CondensSat_Tempter` float(255,0) DEFAULT NULL,
  `Vehicle_load` float(255,0) DEFAULT NULL,
  `Return_Air_Mean_Temper` float(255,0) DEFAULT NULL,
  `Outlet_Air_MeanTemper` float DEFAULT NULL,
  `Fresh_Air_MeanTemper` float DEFAULT NULL,
  `Return_Air_HotSpot_Temper` float DEFAULT NULL,
  `Outlet_HotSpot_Temper` float(255,0) DEFAULT NULL,
  `Return_Air_MeanHumidity` float(255,0) DEFAULT NULL,
  `Control_Temper` float DEFAULT NULL,
  `Control_Humidity` float DEFAULT NULL,
  `Dew_Point_Humidity` float DEFAULT NULL,
  `Return_Air_MeanTemper_T` float DEFAULT NULL,
  `Outlet_Air_MeanTemper_T` float(255,0) DEFAULT NULL,
  `Fresh_Air_MeanTemper_T` float(255,0) DEFAULT NULL,
  `Return_Air_MeanHumidity_T` float DEFAULT NULL,
  `Mean_CariageTemper_T` float DEFAULT NULL,
  `Sys1_Coil1_Outlet_Superheat` float DEFAULT NULL,
  `Sys2_Coil1_Outlet_Superheat` float DEFAULT NULL,
  `Sys1_Coil2_Outlet_Superheat` float DEFAULT NULL,
  `Sys1_Coil2_Outlet_Superheat_0` float DEFAULT NULL,
  `Rail_Mean_humidity30` float DEFAULT NULL,
  `Dynamic_Outlet_PointTemper_Calu` float DEFAULT NULL,
  `Unit_PointTemper_Calu` float(255,0) DEFAULT NULL,
  `Coil_Compressor_Demand` float DEFAULT NULL,
  `Dehumidification_Status` float DEFAULT NULL,
  `FreshValve_Pos_FB1_Calu` float DEFAULT NULL,
  `FreshValve_Pos_FB2_Calu` float DEFAULT NULL,
  `Refrigeration_Feedforward` float DEFAULT NULL,
  `Heat_Feed_Forward` float DEFAULT NULL,
  `Cool_Displacement` float DEFAULT NULL,
  `Heat_Displacement` float DEFAULT NULL,
  `Overall_Power` float DEFAULT NULL,
  `UIC_Temper_Limit` float DEFAULT NULL,
  `Fresh_Valve_Opening` float DEFAULT NULL,
  `Mean_Codens_Mediate_Temper` float DEFAULT NULL,
  `Mean_Evaporation_Mediate_Temper` float(255,0) DEFAULT NULL,
  `Mean_Evaporation_Median_Temper_T` float DEFAULT NULL,
  `Converter1_Frequency` float DEFAULT NULL,
  `Converter2_Frequency` float DEFAULT NULL,
  `EEPROM_Error_Num` float DEFAULT NULL,
  `InterFan_1` float DEFAULT NULL,
  `interFan_2` float DEFAULT NULL,
  `OuterFan_1` float DEFAULT NULL,
  `OuterFan_2` float DEFAULT NULL,
  `Compressor_1` float DEFAULT NULL,
  `Compressor_2` float DEFAULT NULL,
  `Return_Air_Valve` float DEFAULT NULL,
  `Fresh_Air_Valve` float DEFAULT NULL,
  `Eleic_Expan_Valve_1` float DEFAULT NULL,
  `Eleic_Expan_Valve_2` float DEFAULT NULL,
  `Eleic_Expan_Valve_3` float DEFAULT NULL,
  `Eleic_Expan_Valve_4` float DEFAULT NULL,
  `Fresh_Alve_Demend` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=813244 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for run_status
-- ----------------------------
DROP TABLE IF EXISTS `run_status`;
CREATE TABLE `run_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键(自增长)',
  `Metro_Line_No` varchar(255) DEFAULT NULL COMMENT '线路号',
  `Train_Type` varchar(255) DEFAULT NULL COMMENT '列车型号',
  `TrainNo` varchar(11) DEFAULT NULL COMMENT '列车号',
  `CarriageNo` varchar(255) DEFAULT NULL COMMENT '车厢号',
  `UnitNo` varchar(255) DEFAULT NULL COMMENT '机组号',
  `HappenTime` datetime DEFAULT NULL COMMENT '发生时间',
  `Version` varchar(255) DEFAULT NULL COMMENT '软件版本',
  `Software_Coding` varchar(255) DEFAULT NULL COMMENT '软件编码',
  `Param_Version` varchar(255) DEFAULT NULL COMMENT '参数表版本',
  `Sys1_Defrosting_Status` int(11) DEFAULT NULL COMMENT '系统1除霜运行状态',
  `Sys2_Defrosting_Status` int(11) DEFAULT NULL COMMENT '系统2除霜运行状态',
  `Dehumidification_Status` int(11) DEFAULT NULL COMMENT '除湿运行状态',
  `Control_Source` varchar(255) DEFAULT NULL COMMENT '控制源',
  `Work_Mode` varchar(255) DEFAULT NULL COMMENT '工作模式',
  `Hot_Start_Flag` varchar(255) DEFAULT NULL COMMENT '热启动标识',
  `Issue_Temper_Offset` int(11) DEFAULT NULL COMMENT '下发温度偏置',
  `Train_Num` varchar(255) DEFAULT NULL COMMENT '列车号',
  `Carriage_Num` varchar(255) DEFAULT NULL COMMENT '车厢号',
  `Inter_Fan1` int(11) DEFAULT NULL COMMENT '内风机1',
  `Inter_Fan2` int(11) DEFAULT NULL COMMENT '内风机2',
  `Outer_Fan1` int(11) DEFAULT NULL COMMENT '外风机1',
  `Outer_Fan2` int(11) DEFAULT NULL COMMENT '外风机2',
  `Compressor1_Runntime` varchar(255) DEFAULT NULL COMMENT '压缩机1运行时间',
  `Compressor2_Runntime` varchar(255) DEFAULT NULL COMMENT '压缩机2运行时间',
  `Elec_Heating1_Runntime` varchar(255) DEFAULT NULL COMMENT '电加热1运行时间',
  `Elec_Heating2_Runntime` varchar(255) DEFAULT NULL COMMENT '电加热2运行时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for alarm_log
-- ----------------------------
DROP TABLE IF EXISTS `alarm_log`;
CREATE TABLE `alarm_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键(自增长)',
  `Metro_Line_No` varchar(255) DEFAULT NULL COMMENT '线路号',
  `Train_Type` varchar(255) DEFAULT NULL COMMENT '列车型号',
  `TrainNo` varchar(11) DEFAULT NULL COMMENT '列车号',
  `CarriageNo` varchar(255) DEFAULT NULL COMMENT '车厢号',
  `UnitNo` varchar(255) DEFAULT NULL COMMENT '机组号',
  `HappenTime` datetime DEFAULT NULL COMMENT '发生时间',
  `Sensor1_ReturnTemper_Failure` int(11) DEFAULT NULL COMMENT '回风温感1失效',
  `Sensor2_ReturnTemper_Failure` int(11) DEFAULT NULL COMMENT '回风温感2失效',             
  `Sensor1_FreshTemper_Failure` int(11) DEFAULT NULL  COMMENT  '新风温感1失效',
  `Sensor2_FreshTemper_Failure` int(11) DEFAULT NULL COMMENT '新风温感2失效',              
  `Sensor1_SupplyTemper_Failure` int(11) DEFAULT NULL COMMENT '送风温感1失效',             
  `Sensor2_SupplyTemper_Failure` int(11) DEFAULT NULL COMMENT '送风温感2失效',
  `Evaporator1_MedTemper1_Failure` int(11) DEFAULT NULL COMMENT '蒸发器1中点温感1失效',
  `Evaporator1_MedTemper2_Failure` int(11) DEFAULT NULL COMMENT '蒸发器1中点温感2失效',
  `Evaporator2_MedTemper1_Failure` int(11) DEFAULT NULL COMMENT '蒸发器2中点温感1失效',
  `Evaporator2_MedTemper2_Failure` int(11) DEFAULT NULL COMMENT '蒸发器2中点温感2失效',
  `Evaporator1_OutletTemper1_Failure` int(11) DEFAULT NULL COMMENT '蒸发器1出口温感1失效',
  `Evaporator1_OutletTemper2_Failure` int(11) DEFAULT NULL COMMENT '蒸发器1出口温感2失效',
  `Evaporator2_OutletTemper1_Failure` int(11) DEFAULT NULL COMMENT '蒸发器2出口温感1失效',
  `Evaporator2_OutletTemper2_Failure` int(11) DEFAULT NULL COMMENT '蒸发器2出口温感2失效',
  `Condenser1_TemperFailure` int(11) DEFAULT NULL COMMENT '冷凝器1温感失效',
  `Condenser2_TemperFailure` int(11) DEFAULT NULL COMMENT '冷凝器2温感失效',
  `Sys1_SuctionTemper_Failure` int(11) DEFAULT NULL COMMENT '系统1吸气温度失效',
  `Sys2_SuctionTemper_Failure` int(11) DEFAULT NULL COMMENT '系统2吸气温度失效',
  `Sys1_ExhaustTemper_Failure` int(11) DEFAULT NULL COMMENT '系统1排气温度失效',
  `Sys2_ExhaustTemper_Failure` int(11) DEFAULT NULL COMMENT '系统2排气温度失效',
  `Sys1_LowPressure_Failure` int(11) DEFAULT NULL COMMENT '系统1低压压力失效',
  `Sys2_LowPressure_Failure` int(11) DEFAULT NULL COMMENT '系统2低压压力失效',
  `Sys1_HighPressure_Failure` int(11) DEFAULT NULL COMMENT '系统1高压压力失效',
  `Sys2_HighPressure_Failure` int(11) DEFAULT NULL COMMENT '系统2高压压力失效',
  `Sys1_CondensPressure_Failure` int(11) DEFAULT NULL COMMENT '系统1冷凝压力失效',
  `Sys2_CondensPressure_Failure` int(11) DEFAULT NULL COMMENT '系统2冷凝压力失效',
  `PassagerTemper1_Failure` int(11) DEFAULT NULL COMMENT '客室温度1失效',
  `PassagerTemper2_Failure` int(11) DEFAULT NULL COMMENT '客室温度2失效',
  `PassagerHumidity1_Failure` int(11) DEFAULT NULL COMMENT '客室湿度1失效',
  `PassagerHumidity2_Failure` int(11) DEFAULT NULL COMMENT '客室湿度2失效',
  `UnitTemper1_Failure` int(11) DEFAULT NULL COMMENT '机组温度1失效',
  `UnitTemper2_Failure` int(11) DEFAULT NULL COMMENT '机组温度2失效',
  `UnitHumidity1_Failure` int(11) DEFAULT NULL COMMENT '机组湿度1失效',
  `UnitHumidity2_Failure` int(11) DEFAULT NULL COMMENT '机组湿度2失效',
  `Sys1_Antifreeze_Protect` int(11) DEFAULT NULL COMMENT '系统1制冷时盘管防冻保护',
  `Sys2_Antifreeze_Protect` int(11) DEFAULT NULL COMMENT '系统2制冷时盘管防冻保护',
  `Sys1_Abnormal` int(11) DEFAULT NULL COMMENT '系统1系统异常',
  `Sys2_Abnormal` int(11) DEFAULT NULL COMMENT '系统2系统异常',
  `Sys1_ShortAlarm` int(11) DEFAULT NULL COMMENT '系统1短周期报警',
  `Sys2_ShortAlarm` int(11) DEFAULT NULL COMMENT '系统2短周期报警',
  `Sys1_LowSuperHeat_Protect` int(11) DEFAULT NULL COMMENT '系统1低过热度保护',
  `Sys2_LowSuperHeat_Protect` int(11) DEFAULT NULL COMMENT '系统2低过热度保护',
  `Sys1_HigPressure_Alarm` int(11) DEFAULT NULL COMMENT '系统1高压告警',
  `Sys2_HigPressure_Alarm` int(11) DEFAULT NULL COMMENT '系统2高压告警',
  `Sys1_LowPressure_Alarm` int(11) DEFAULT NULL COMMENT '系统1低压告警',
  `Sys2_LowPressure_Alarm` int(11) DEFAULT NULL COMMENT '系统2低压告警',
  `Sys1_ExhaustTemper_High` int(11) DEFAULT NULL COMMENT '系统1排气温度过高',
  `Sys2_ExhaustTemper_High` int(11) DEFAULT NULL COMMENT '系统2排气温度过高',
  `Interfan1_Internalthermal_Protect` int(11) DEFAULT NULL COMMENT '内风机1内部热保护',
  `Interfan2_Internalthermal_Protect` int(11) DEFAULT NULL COMMENT '内风机2内部热保护',
  `Interfan1_MaProtect` int(11) DEFAULT NULL COMMENT '内风机1马保保护',
  `Interfan2_MaProtect` int(11) DEFAULT NULL COMMENT '内风机2马保保护',
  `Outerfan1_Internalthermal_Protect` int(11) DEFAULT NULL COMMENT '外风机1内部热保护',
  `Outerfan2_Internalthermal_Protect` int(11) DEFAULT NULL COMMENT '外风机2内部热保护',
  `Outerfan1_MaProtect` int(11) DEFAULT NULL COMMENT '外风机1马保保护',
  `Outerfan2_MaProtect` int(11) DEFAULT NULL COMMENT '外风机2马保保护',
  `Compressor1_MaProtect` int(11) DEFAULT NULL COMMENT '压缩机1马保保护',
  `Compressor2_MaProtect` int(11) DEFAULT NULL COMMENT '压缩机1马保保护',
  `ReturnValve1_Fault` int(11) DEFAULT NULL COMMENT '回风阀1故障',
  `ReturnValve2_Fault` int(11) DEFAULT NULL COMMENT '回风阀2故障',
  `ReturnValve3_Fault` int(11) DEFAULT NULL COMMENT '回风阀3故障',
  `ReturnValve4_Fault` int(11) DEFAULT NULL COMMENT '回风阀4故障',
  `FreshValve1_Fault` int(11) DEFAULT NULL COMMENT '新风阀1故障',
  `FreshValve2_Fault` int(11) DEFAULT NULL COMMENT '新风阀2故障',
  `ThreePhase_PowerFailure` int(11) DEFAULT NULL COMMENT '三相电源故障',
  `EmergencyInverter_Failure` int(11) DEFAULT NULL COMMENT '紧急逆变器故障',
  `Fire_Alarm` int(11) DEFAULT NULL COMMENT '火灾告警',
  `TCMS_Communication_Failure` int(11) DEFAULT NULL COMMENT 'TCMS通讯故障',
  `IO1_Communication_Failure` int(11) DEFAULT NULL COMMENT 'IO板1通讯故障',
  `IO2_Communication_Failure` int(11) DEFAULT NULL COMMENT 'IO板2通讯故障',
  `InterLAN_Communication_Failure` int(11) DEFAULT NULL COMMENT '内部局域网通讯故障',
  `Sys1_Inverter_Connect_Failure` int(11) DEFAULT NULL COMMENT '系统1变频器通讯故障',
  `Sys2_Inverter_Connect_Failure` int(11) DEFAULT NULL COMMENT '系统2变频器通讯故障',
  `Sys1_ElecHeat_Fault` int(11) DEFAULT NULL COMMENT '系统1电加热故障',
  `Sys1_ElecHeat_Fault0` int(11) DEFAULT NULL COMMENT '系统1电加热故障',
  `Sys1_inverter_OverCurrent` int(11) DEFAULT NULL COMMENT '系统1变频器过流',
  `Sys2_inverter_OverCurrent` int(11) DEFAULT NULL COMMENT '系统2变频器过流',
  `Sys1_inverter_OverHeat` int(11) DEFAULT NULL COMMENT '系统1变频器过温',
  `Sys2_inverter_OverHeat` int(11) DEFAULT NULL COMMENT '系统2变频器过温',
  `Sys1_inverter_OverVoltage` int(11) DEFAULT NULL COMMENT '系统1变频器过压',
  `Sys2_inverter_OverVoltage` int(11) DEFAULT NULL COMMENT '系统2变频器过压',
  `Sys1_inverter_UnderVoltage` int(11) DEFAULT NULL COMMENT '系统1变频器欠压',
  `Sys2_inverter_UnderVoltage` int(11) DEFAULT NULL COMMENT '系统2变频器欠压',
  `Sys1_inverter_LossPhase` int(11) DEFAULT NULL COMMENT '系统1变频器缺相',
  `Sys2_inverter_LossPhase` int(11) DEFAULT NULL COMMENT '系统2变频器缺相',
  `Sys1_inverter_OtherFault` int(11) DEFAULT NULL COMMENT '系统1变频器其它故障',
  `Sys2_inverter_OtherFault` int(11) DEFAULT NULL COMMENT '系统2变频器其它故障',
  `Sys1_HV_AlarmLock` int(11) DEFAULT NULL COMMENT '系统1高压告警锁定',
  `Sys2_HV_AlarmLock` int(11) DEFAULT NULL COMMENT '系统2高压告警锁定',
  `Sys1_LV_AlarmLock` int(11) DEFAULT NULL COMMENT '系统1低压告警锁定',
  `Sys2_LV_AlarmLock` int(11) DEFAULT NULL COMMENT '系统2低压告警锁定',
  `Sys1_ExhaustTemper_Hlock` int(11) DEFAULT NULL COMMENT '系统1排气温度过高锁定',
  `Sys2_ExhaustTemper_Hlock` int(11) DEFAULT NULL COMMENT '系统2排气温度过高锁定',
  `Sys1_Inverter_HCurrlock` int(11) DEFAULT NULL COMMENT '系统1变频器过流锁定',
  `Sys2_Inverter_HCurrlock` int(11) DEFAULT NULL COMMENT '系统2变频器过流锁定',
  `Sys1_Inverter_HTemperlock` int(11) DEFAULT NULL COMMENT '系统1变频器过温锁定',
  `Sys2_Inverter_HTemperlock` int(11) DEFAULT NULL COMMENT '系统2变频器过温锁定',
  `Sys1_Inverter_HVollock` int(11) DEFAULT NULL COMMENT '系统1变频器过压锁定',
  `Sys2_Inverter_HVollock` int(11) DEFAULT NULL COMMENT '系统2变频器过压锁定',
  `Sys1_Inverter_LVollock` int(11) DEFAULT NULL COMMENT '系统1变频器欠压锁定',
  `Sys2_Inverter_LVollock` int(11) DEFAULT NULL COMMENT '系统2变频器欠压锁定',
  `Sys1_Inverter_MissPhasslock` int(11) DEFAULT NULL COMMENT '系统1变频器缺相锁定',
  `Sys2_Inverter_MissPhasslock` int(11) DEFAULT NULL COMMENT '系统2变频器缺相锁定',
  `Sys1_Inverter_OtherFaultlock` int(11) DEFAULT NULL COMMENT '系统1变频器其他故障锁定',
  `Sys2_Inverter_OtherFaultlock` int(11) DEFAULT NULL COMMENT '系统2变频器其他故障锁定',
  `Sys1_AntiFreezeAlarm_Hot` int(11) DEFAULT NULL COMMENT '系统1制热时盘管防冻告警',
  `Sys2_AntiFreezeAlarm_Hot` int(11) DEFAULT NULL COMMENT '系统2制热时盘管防冻告警',
  `Sys1_LVol_SwitchAlarm` int(11) DEFAULT NULL COMMENT '系统1低压开关告警',
  `Sys2_LVol_SwitchAlarm` int(11) DEFAULT NULL COMMENT '系统2低压开关告警',
  `MVB_NetConnect_Fault` int(11) DEFAULT NULL COMMENT 'MVB网络通讯故障',
  `Sys1_LVol_AlarmLock` int(11) DEFAULT NULL COMMENT '系统1低压告警锁定',
  `Sys2_LVol_AlarmLock` int(11) DEFAULT NULL COMMENT '系统2低压告警锁定',
  `InterFan1_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '内风机1接触器反馈故障',
  `InterFan2_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '内风机2接触器反馈故障',
  `OuterFan1_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '外风机1接触器反馈故障',
  `OuterFan2_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '外风机2接触器反馈故障',
  `Compressor1_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '压机1接触器反馈故障',
  `Compressor2_ContactorFD_Fault` int(11) DEFAULT NULL COMMENT '压机2接触器反馈故障',
  `ElecHeat1_LockAlarm` int(11) DEFAULT NULL COMMENT '电加热1锁定告警',
  `ElecHeat2_LockAlarm` int(11) DEFAULT NULL COMMENT '电加热2锁定告警',
  `InterFan1_ContactorLock_Alarm` int(11) DEFAULT NULL COMMENT '内风机1接触器锁定告警',
  `InterFan2_ContactorLock_Alarm` int(11) DEFAULT NULL COMMENT '内风机2接触器锁定告警',

  `FreshValve1_Alarm` float DEFAULT NULL COMMENT '新风阀1告警',
  `FreshValve2_Alarm` float DEFAULT NULL COMMENT '新风阀2告警',
  `FreshValve3_Alarm` float DEFAULT NULL COMMENT '新风阀3告警',
  `FreshValve4_Alarm` float DEFAULT NULL COMMENT '新风阀4告警',
  `NoramlVenti_Contactor_FDFault` int(11) DEFAULT NULL COMMENT '正常通风接触器反馈故障',
  `NoramlVenti_Contactor_FDFaultLock` int(11) DEFAULT NULL COMMENT '正常通风接触器反馈故障锁定',
  `MainPower_Fault` int(11) DEFAULT NULL COMMENT '主电源故障',
  `Em_VentiPower_OpenAlarm` int(11) DEFAULT NULL COMMENT '紧急通风电源空开告警',
  `DriverRoom_Power_OpenAlarm` int(11) DEFAULT NULL COMMENT '司机室电源空开告警',
  `MainPower_OpenAlarm` int(11) DEFAULT NULL COMMENT '主电源空开告警',
  `Sys1_Refrigerant_Leakage` int(11) DEFAULT NULL COMMENT '系统1冷媒泄露',
  `Sys2_Refrigerant_Leakage` int(11) DEFAULT NULL COMMENT '系统2冷媒泄露',
  `Compressor_Safe_HighPression1` int(11) DEFAULT NULL COMMENT '压机安全高压1',
  `Compressor_Safe_HighPression2` int(11) DEFAULT NULL COMMENT '压机安全高压2',
  `Compressor1_InterProtection` int(11) DEFAULT NULL COMMENT '压缩机1内保护',
  `Compressor2_InterProtection` int(11) DEFAULT NULL COMMENT '压缩机2内保护',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for AlmRecord 
-- ----------------------------
DROP TABLE IF EXISTS `AlmRecord`;
CREATE TABLE `AlmRecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键(自增长)',
  `Metro_Line_No` varchar(255) DEFAULT NULL COMMENT '线路号',
  `Train_Type` varchar(255) DEFAULT NULL COMMENT '列车型号',
  `TrainNo` varchar(11) DEFAULT NULL COMMENT '列车号',
  `CarriageNo` varchar(255) DEFAULT NULL COMMENT '车厢号',
  `UnitNo` varchar(255) DEFAULT NULL COMMENT '机组号',
  `HappenTime` datetime DEFAULT NULL COMMENT '发生时间',
  `Action` varchar(255) DEFAULT NULL COMMENT '动作',
  `Alarm_Content` varchar(255) DEFAULT NULL COMMENT '告警内容',
  `Level` varchar(11) DEFAULT NULL COMMENT '等级',
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;




-- ----------------------------
-- Table structure for heath_status
-- ----------------------------
DROP TABLE IF EXISTS `heath_status`;
CREATE TABLE `heath_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键(自增长)',
  `Metro_Line_No` varchar(255) DEFAULT NULL COMMENT '线路号',
  `Train_Type` varchar(255) DEFAULT NULL COMMENT '列车型号',
  `TrainNo` varchar(11) DEFAULT NULL COMMENT '列车号',
  `CarriageNo` varchar(255) DEFAULT NULL COMMENT '车厢号',
  `UnitNo` varchar(255) DEFAULT NULL COMMENT '机组号',
  `HappenTime` datetime DEFAULT NULL COMMENT '发生时间',
  `HealthValue` float DEFAULT NULL COMMENT '健康值',
  `HealthLevel` int(11) DEFAULT NULL COMMENT '健康等级',                  
  `Suggest` varchar(255) DEFAULT NULL COMMENT '维修建议',
  `HandleStatus` int(11) DEFAULT NULL COMMENT '处理状态',                 
  `Handler` varchar(255) DEFAULT NULL COMMENT '处理人',                   
  `HandleTime` datetime DEFAULT NULL COMMENT '处理时间',
  `FaultResult` varchar(255) DEFAULT NULL COMMENT '故障原因',
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;







