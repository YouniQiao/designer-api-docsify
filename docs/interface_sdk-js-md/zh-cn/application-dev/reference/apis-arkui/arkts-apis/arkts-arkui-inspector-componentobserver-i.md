# ComponentObserver

组件布局和组件绘制送显完成回调的句柄，通过该句柄可调用以下方法。

**起始版本：** 10

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## off('layout')

```TypeScript
off(type: 'layout', callback?: () => void): void
```

通过句柄取消注册回调，当组件布局完成时不再触发指定的回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'layout' | 是 |
| callback | () = & gt; void | 否 |

## off('draw')

```TypeScript
off(type: 'draw', callback?: () => void): void
```

通过句柄取消注册回调，当组件绘制送显完成时不再触发指定的回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'draw' | 是 |
| callback | () = & gt; void | 否 |

## off('drawChildren')

```TypeScript
off(type: 'drawChildren', callback?: Callback<void>): void
```

通过句柄取消注册回调，当组件的子组件绘制送显完成时不再触发指定的回调。如果组件树中存在多个drawChildren事件回调，取消最顶层的回调后，其余drawChildren事件回调也无法生效。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'drawChildren' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## offDrawChildren

```TypeScript
offDrawChildren(callback?: Callback<number[]>): void
```

取消注册drawChildren事件回调。要实现在子组件绘制送显完成后停止触发特定回调，只需通过ComponentObserver句柄，取消注册该回调即可。 如果组件树中存在多个drawChildren事件回调，取消最顶层的回调后，其余drawChildren事件回调也无法生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number[]&gt; | 否 |

## offLayoutChildren

```TypeScript
offLayoutChildren(callback?: Callback<void>): void
```

取消注册layoutChildren事件回调。要实现在子组件布局完成后停止触发特定回调，只需通过ComponentObserver句柄，取消注册该回调即可。 如果组件树中存在多个layoutChildren事件回调，取消最顶层的回调后，其余layoutChildren事件回调也无法生效。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## on('layout')

```TypeScript
on(type: 'layout', callback: () => void): void
```

通过句柄向对应的查询条件注册回调，当组件布局完成时会触发该回调。请注意，该接口无法监听窗口尺寸变化，相关需求请参考on('windowSizeChange')。此外，布局回调和窗口尺寸变化回调之间不存在确定的执行顺序依赖。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'layout' | 是 |
| callback | () = & gt; void | 是 |

## on('draw')

```TypeScript
on(type: 'draw', callback: () => void): void
```

通过句柄注册回调，当组件绘制送显完成时会触发该回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'draw' | 是 |
| callback | () = & gt; void | 是 |

## on('drawChildren')

```TypeScript
on(type: 'drawChildren', callback: Callback<void>): void
```

通过ComponentObserver注册drawChildren事件回调方法。当组件的子组件位于UI组件主树中且绘制送显完成时，会触发该回调方法。 如果组件树中存在多个drawChildren事件回调，只会触发最顶层的drawChildren事件回调。取消最顶层的回调后，其余drawChildren事件回调也无法生效。 当前节点注册回调后，不支持修改其在UI组件主树中的层级位置。如需调整，请先取消事件回调，再重新注册事件回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'drawChildren' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## onDrawChildren

```TypeScript
onDrawChildren(callback: Callback<number[]>): void
```

通过ComponentObserver注册drawChildren事件回调。使用callback异步回调。 与on('drawChildren')相比，本方法在回调中额外返回子组件的uniqueId信息（Callback&lt;number[]&gt;），便于开发者定位具体子组件。 如需获取子组件标识，建议使用本方法；若不需要子组件信息，两者均可使用。以当前注册事件回调的节点为根节点，当组件的子组件位于UI组件主树中且绘制送显完成时，会触发该回调。 如果组件树中存在多个drawChildren事件回调，只会触发最顶层的drawChildren事件回调。取消最顶层的回调后，其余drawChildren事件回调也无法生效。 当前节点注册事件回调后，不支持修改其在UI组件主树中的层级位置。如需调整，请先取消事件回调，再重新注册事件回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number[]&gt; | 是 |

## onLayoutChildren

```TypeScript
onLayoutChildren(callback: Callback<void>): void
```

通过ComponentObserver注册layoutChildren事件回调。使用callback异步回调。以当前注册事件回调的节点为根节点，当子树中的节点位于UI组件主树中且完成布局时，会触发该回调。 如果组件树中存在多个layoutChildren事件回调，只会触发最顶层的layoutChildren事件回调。通过offLayoutChildren取消最顶层的回调后，其余layoutChildren事件回调也无法生效。 当前节点注册回调后，不支持修改其在UI组件主树中的层级位置。如需调整，请先取消事件回调，再重新注册事件回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |
