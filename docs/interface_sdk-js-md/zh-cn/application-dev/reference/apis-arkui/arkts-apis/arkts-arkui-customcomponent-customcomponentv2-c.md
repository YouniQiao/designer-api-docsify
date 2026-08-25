# CustomComponentV2

V2自定义组件类的定义。

**继承/实现关系：** CustomComponentV2 extends BaseCustomComponent<T_Options>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: () => string,
        content?: CustomBuilder
    ): void
```

Implementation for creating a v2 custom component

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | 是 |
| factory | () = & gt; S | 是 |
| initializers | () = & gt; S_Options | 否 |
| reuseId | () = & gt; string | 否 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: () => string,
        content?: CustomBuilder,
        options?: CustomComponentInvokeOptions
    ): void
```

Implementation for creating a v2 custom component

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | 是 |
| factory | () = & gt; S | 是 |
| initializers | () = & gt; S_Options | 否 |
| reuseId | () = & gt; string | 否 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |
| options | [CustomComponentInvokeOptions](arkts-arkui-customcomponent-customcomponentinvokeoptions-i.md) | 否 |

## aboutToReuse

```TypeScript
aboutToReuse(): void
```

组件复用时，触发回调

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## resetStateVarsOnReuse

```TypeScript
resetStateVarsOnReuse(params?: T_Options): void
```

重置状态变量

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | T_Options | 否 |
