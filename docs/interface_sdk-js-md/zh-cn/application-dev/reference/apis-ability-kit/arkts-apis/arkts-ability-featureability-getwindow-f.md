# getWindow

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## getWindow

```TypeScript
function getWindow(callback: AsyncCallback<window.Window>): void
```

获取当前Ability对应的窗口。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;window.Window&gt; | 是 |


## getWindow

```TypeScript
function getWindow(): Promise<window.Window>
```

获取当前Ability对应的窗口。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 |
| --- |
| Promise & lt;window.Window & gt; |
