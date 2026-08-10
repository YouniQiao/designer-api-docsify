# InputMethodEngine

下列API均需使用[getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getinputmethodengine)获取到InputMethodEngine实例后，通过实例调用。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** [inputMethodEngine.InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)

<!--Device-inputMethodEngine-interface InputMethodEngine--><!--Device-inputMethodEngine-interface InputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## off('inputStart')

```TypeScript
off(
      type: 'inputStart',
      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void
    ): void
```

取消订阅输入法绑定成功事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.off(type:

<!--Device-InputMethodEngine-off(      type: 'inputStart',      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void--><!--Device-InputMethodEngine-off(      type: 'inputStart',      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine()
  .off('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      console.info('delete inputStart notification.');
    });
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.off(type:

<!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 要取消监听的输入法软键盘事件类型。&lt;br/&gt;-'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;-' keyboardHide'表示隐藏输入法软键盘。 |
| callback | () =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.off(type:

<!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 要取消监听的输入法软键盘事件类型。&lt;br/&gt;-'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;-' keyboardHide'表示隐藏输入法软键盘。 |
| callback | () =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

## on('inputStart')

```TypeScript
on(
      type: 'inputStart',
      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void
    ): void
```

订阅输入法绑定成功事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.on(type:

<!--Device-InputMethodEngine-on(      type: 'inputStart',      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void--><!--Device-InputMethodEngine-on(      type: 'inputStart',      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) =&gt; void | Yes | 回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let textInputClient: inputMethodEngine.TextInputClient = textClient;
    });
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.on(type:

<!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;-'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;-'keyboardHide'表示隐藏输 入法软键盘。 |
| callback | () =&gt; void | Yes | 回调函数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 23

**Substitutes:** inputMethodEngine.InputMethodAbility.on(type:

<!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;-'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;-'keyboardHide'表示隐藏输 入法软键盘。 |
| callback | () =&gt; void | Yes | 回调函数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});
```

