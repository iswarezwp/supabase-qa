'use client'
import { useState } from "react"
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'
import { FaPaperPlane, FaSpinner } from 'react-icons/fa';

interface Message {
    sender: string;
    text: string;
}

export default function QAPage() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);

    const appendMessage = (msg: Message) => {
        setMessages((prevMessages) => [...prevMessages, msg])
    }

    const sendMessage = () => {
        const messageInput: HTMLInputElement = document.getElementById('message-input') as HTMLInputElement;
        const message = messageInput?.value?.trim();
        if (message.length == 0) {
            return
        }

        appendMessage({'sender': 'user', text: message})
        messageInput.value = '';

        setLoading(true);
        const apiUrl = '/api/v1/qa/ask';
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "question": message }),
        })
        .then((response) => {
            setLoading(false);
            if (!response.ok) {
                throw new Error("HTTP Request Error");
            }
            return response.json();
        })
        .then((data) => {
            console.log('Table definition posted successfully:', data);
            appendMessage({'sender': 'ai', text: data['result']})
        })
        .catch((error) => {
            setLoading(false);
            console.error('Error posting table definition:', error);
            appendMessage({'sender': 'ai', text: '请求失败'})
        });

    };

    const handleKeyDown = (event: any) => {
        if (event.key === 'Enter') {
          sendMessage();
        }
    };

    return (
        <div className="h-screen flex flex-col justify-between bg-gray-100">
            <div className="p-4 flex-1 overflow-y-auto">
                {messages.map((message, index) => (
                <div
                    key={index}
                    className={`p-2 rounded ${message.sender === 'user' ? 'bg-blue-500 text-white self-end' : 'bg-white text-gray-800 self-start'}`}
                >
                    <ReactMarkdown remarkPlugins={[remarkGfm]}>{message.text}</ReactMarkdown>

                </div>
                ))}
            </div>
            <div className="p-4 flex items-center">
                <input
                id="message-input"
                type="text"
                placeholder="请输入你的问题..."
                className="flex-1 p-2 border rounded"
                onKeyDown={handleKeyDown}
                disabled={loading}
                />
                <button
                className="ml-2 px-4 py-2 bg-blue-500 text-white rounded"
                disabled={loading}
                onClick={sendMessage}
                >
                    {loading ? <FaSpinner className="mr-1 animate-spin" /> : <FaPaperPlane className="mr-1" />}
                </button>
            </div>
        </div>
    )
}