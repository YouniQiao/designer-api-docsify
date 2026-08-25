# off

## 导入模块

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## off('prepareContinue')

```TypeScript
function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

在应用快速拉起时，注销回调函数，不再获取快速拉起结果。使用callback异步回调。适用于跨设备应用迁移完成或取消迁移后的回调清理场景，如应用迁移成功后清理监听、用户取消迁移操作时释放资源等。说明：快速拉起功能支持在用户触发迁移、等待迁移数据返回的过程中，并行拉起应用，减小用户等待时间。在源端应用module.json5配置文件的continueType标签的取值中添加"_ContinueQuickStart"后缀，可以开启快速拉起功能。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'prepareContinue' | 是 |
| context | [Context](arkts-ability-context-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
