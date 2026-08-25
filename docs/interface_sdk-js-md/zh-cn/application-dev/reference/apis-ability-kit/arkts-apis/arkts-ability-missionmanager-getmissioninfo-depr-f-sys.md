# getMissionInfo（系统接口）

## 导入模块

```TypeScript
```

## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number, callback: AsyncCallback<MissionInfo>): void
```

获取单个任务信息。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| missionId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt; | 是 |


## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number): Promise<MissionInfo>
```

获取单个任务信息。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| missionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt; |
