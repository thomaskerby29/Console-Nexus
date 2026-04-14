import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Console Nexus"

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    ColumnLayout {
        spacing: 2
        anchors.fill:  parent

        Text {
            text: "Setup"
            font.pixelSize: 30
            font.bold: true
            Layout.alignment: Qt.AlignHCenter
        }

        Text {
            id: text
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }

    }
}