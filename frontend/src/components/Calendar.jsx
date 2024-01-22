import React, { useState } from 'react';

const Calendar = () => {
  const [currentMonth, setCurrentMonth] = useState(new Date());


  const getDaysInMonth = (date) => {
    const firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
    const daysInMonth = [];

    for (let day = firstDay; day <= lastDay; day.setDate(day.getDate() + 1)) {
      daysInMonth.push(new Date(day));
    }

    return daysInMonth;
  };

  const renderDays = () => {
    const daysInMonth = getDaysInMonth(currentMonth);

    return daysInMonth.map((day) => (
      <div key={day.toISOString()} className="calendar-day">
        {day.getDate()}
      </div>
    ));
  };

  const goToPreviousMonth = () => {
    const previousMonth = new Date(currentMonth);
    previousMonth.setMonth(currentMonth.getMonth() - 1);
    setCurrentMonth(previousMonth);
  };

  const goToNextMonth = () => {
    const nextMonth = new Date(currentMonth);
    nextMonth.setMonth(currentMonth.getMonth() + 1);
    setCurrentMonth(nextMonth);
  };

  return (
    <div className="calendar-container">
      <div className="calendar-header">
        <button onClick={goToPreviousMonth}>&lt;</button>
        <h2>{currentMonth.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</h2>
        <button onClick={goToNextMonth}>&gt;</button>
      </div>
      <div className="calendar-grid">
        {renderDays()}
      </div>
    </div>
  );
};

export default Calendar;
