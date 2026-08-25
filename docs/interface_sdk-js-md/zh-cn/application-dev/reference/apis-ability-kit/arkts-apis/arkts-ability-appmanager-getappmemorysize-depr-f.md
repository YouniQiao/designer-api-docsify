# getAppMemorySize

## 导入模块

```TypeScript
```

## getAppMemorySize

```TypeScript
function getAppMemorySize(): Promise<number>
```

获取当前应用程序可以使用的最大内存（RAM）值。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |


## getAppMemorySize

```TypeScript
function getAppMemorySize(callback: AsyncCallback<number>): void
```

获取当前应用程序可以使用的最大内存（RAM）值。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
