# UIExtensionProxy (System API)

Implements a **UIExtensionProxy** instance for the component host to send data to, subscribe to, or unsubscribe from the started UIExtensionAbility through the connection established between the two parties.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare interface UIExtensionProxy--><!--Device-unnamed-declare interface UIExtensionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## off_asyncReceiverRegister

```TypeScript
off(type: 'asyncReceiverRegister', callback?: Callback<UIExtensionProxy>): void
```

Unsubscribes from asynchronous registration of the started UIExtensionAbility through the connection established between the component host and UIExtensionAbility.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-off(type: 'asyncReceiverRegister', callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-off(type: 'asyncReceiverRegister', callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'asyncReceiverRegister' | Yes |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | No |

## off_syncReceiverRegister

```TypeScript
off(type: 'syncReceiverRegister', callback?: Callback<UIExtensionProxy>): void
```

Unsubscribes from synchronous registration of the started UIExtensionAbility through the connection established between the component host and UIExtensionAbility.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-off(type: 'syncReceiverRegister', callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-off(type: 'syncReceiverRegister', callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'syncReceiverRegister' | Yes |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | No |

## on_asyncReceiverRegister

```TypeScript
on(type: 'asyncReceiverRegister', callback: Callback<UIExtensionProxy>): void
```

Subscribes to asynchronous registration of the started UIExtensionAbility through the connection established between the component host and UIExtensionAbility.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-on(type: 'asyncReceiverRegister', callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-on(type: 'asyncReceiverRegister', callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'asyncReceiverRegister' | Yes |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | Yes |

## on_syncReceiverRegister

```TypeScript
on(type: 'syncReceiverRegister', callback: Callback<UIExtensionProxy>): void
```

Subscribes to synchronous registration of the started UIExtensionAbility through the connection established between the component host and UIExtensionAbility.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-on(type: 'syncReceiverRegister', callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-on(type: 'syncReceiverRegister', callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'syncReceiverRegister' | Yes |
| callback | Callback&lt;[UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)&gt; | Yes |

## send

```TypeScript
send(data: Record<string, Object>): void
```

Asynchronously sends data from the component host to the started UIExtensionAbility through the connection established between the two parties.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-send(data: Record<string, Object>): void--><!--Device-UIExtensionProxy-send(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | Yes |

## sendSync

```TypeScript
sendSync(data: Record<string, Object>): Record<string, Object>
```

Synchronously sends data from the component host to the started UIExtensionAbility through the connection established between the two parties.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-sendSync(data: Record<string, Object>): Record<string, Object>--><!--Device-UIExtensionProxy-sendSync(data: Record<string, Object>): Record<string, Object>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| object |
| [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100011](../errorcode-uiextension.md#100011-no-synchronous-callback-registered) |
| [100012](../errorcode-uiextension.md#100012-data-transfer-failure) |
