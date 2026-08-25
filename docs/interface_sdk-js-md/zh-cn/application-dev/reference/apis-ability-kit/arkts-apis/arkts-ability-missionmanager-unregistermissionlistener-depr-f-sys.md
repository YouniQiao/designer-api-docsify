# unregisterMissionListener（系统接口）

## 导入模块

```TypeScript
```

## unregisterMissionListener

```TypeScript
function unregisterMissionListener(listenerId: number, callback: AsyncCallback<void>): void
```

解注册任务状态监听器。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-ability-missionmanager-off-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listenerId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## unregisterMissionListener

```TypeScript
function unregisterMissionListener(listenerId: number): Promise<void>
```

解注册任务状态监听器。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-ability-missionmanager-off-f-sys.md)

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listenerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
