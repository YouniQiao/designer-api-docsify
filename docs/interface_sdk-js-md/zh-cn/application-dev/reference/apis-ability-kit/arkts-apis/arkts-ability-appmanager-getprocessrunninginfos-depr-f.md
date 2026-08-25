# getProcessRunningInfos

## 导入模块

```TypeScript
```

## getProcessRunningInfos

```TypeScript
function getProcessRunningInfos(): Promise<Array<ProcessRunningInfo>>
```

获取有关运行进程的信息。使用Promise异步回调。

> 从 API Version 9 开始废弃，建议使用
> [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md)

**需要权限：** ohos.permission.GET_RUNNING_INFO

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ProcessRunningInfo](arkts-ability-processrunninginfo-i.md)&gt;&gt; |


## getProcessRunningInfos

```TypeScript
function getProcessRunningInfos(callback: AsyncCallback<Array<ProcessRunningInfo>>): void
```

获取有关运行进程的信息。使用callback异步回调。

> 从 API Version 9 开始废弃，建议使用
> [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md)

**需要权限：** ohos.permission.GET_RUNNING_INFO

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessRunningInfo](arkts-ability-processrunninginfo-i.md)&gt;&gt; | 是 |
