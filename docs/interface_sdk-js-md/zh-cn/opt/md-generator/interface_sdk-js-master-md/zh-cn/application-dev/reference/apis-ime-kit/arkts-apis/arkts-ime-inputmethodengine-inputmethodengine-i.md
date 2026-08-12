# InputMethodEngine

下列API均需使用[getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getInputMethodEngine)获取到InputMethodEngine实例后，通过实例调用。

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md#InputMethodAbility)

<!--Device-inputMethodEngine-interface InputMethodEngine--><!--Device-inputMethodEngine-interface InputMethodEngine-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## off('inputStart')

```TypeScript
off(
      type: 'inputStart',
      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void
    ): void
```

取消订阅输入法绑定成功事件。

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [off](inputMethodEngine.InputMethodAbility.off(type:)

<!--Device-InputMethodEngine-off(      type: 'inputStart',      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void--><!--Device-InputMethodEngine-off(      type: 'inputStart',      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStart' | 是 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) = & gt; void | 否 |

## 示例

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

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [off](inputMethodEngine.InputMethodAbility.off(type:)

<!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 否 |

## 示例

```TypeScript
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [off](inputMethodEngine.InputMethodAbility.off(type:)

<!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodEngine-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 否 |

## 示例

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

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [on](inputMethodEngine.InputMethodAbility.on(type:)

<!--Device-InputMethodEngine-on(      type: 'inputStart',      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void--><!--Device-InputMethodEngine-on(      type: 'inputStart',      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void    ): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStart' | 是 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) = & gt; void | 是 |

## 示例

```TypeScript
inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (keyboardController: inputMethodEngine.KeyboardController, textInputClient: inputMethodEngine.TextInputClient) => {
      // 使用kbController和textClient进行相关操作
    });
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [on](inputMethodEngine.InputMethodAbility.on(type:)

<!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 是 |

## 示例

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

**起始版本：** 8

**废弃版本：** 23

**替代接口：** [on](inputMethodEngine.InputMethodAbility.on(type:)

<!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodEngine-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 是 |

## 示例

```TypeScript
inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});
```
