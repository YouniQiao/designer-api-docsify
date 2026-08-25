# clearMission（系统接口）

## 导入模块

```TypeScript
```

## clearMission

```TypeScript
function clearMission(missionId: number, callback: AsyncCallback<void>): void
```

清理指定任务id的任务，无论该任务是否被锁定。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clearMission](arkts-ability-missionmanager-clearmission-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## clearMission

```TypeScript
function clearMission(missionId: number): Promise<void>
```

清理指定任务id的任务，无论该任务是否被锁定。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clearMission](arkts-ability-missionmanager-clearmission-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
